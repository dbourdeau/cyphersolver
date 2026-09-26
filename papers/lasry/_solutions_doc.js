// Lays out the solutions list as a Word file from the payload written by _solutions_list.py.
//   node _solutions_doc.js <payload.json> <out.docx>
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, ExternalHyperlink, HeadingLevel, Table, TableRow, TableCell,
  WidthType, BorderStyle, ShadingType, LevelFormat, AlignmentType, Footer, PageNumber,
} = require('docx');

const [, , payloadPath, outPath] = process.argv;
const P = JSON.parse(fs.readFileSync(payloadPath, 'utf8'));

const FONT = 'Georgia';
const TABLE_W = 9026;               // A4 text width with 1-inch margins, in DXA
const LABEL_W = 2100;
const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: none, bottom: none, left: none, right: none, insideHorizontal: none, insideVertical: none };

function textRuns(runs, size) {
  return runs.map(r => r.url
    ? new ExternalHyperlink({ link: r.url, children: [new TextRun({ text: r.t, style: 'Hyperlink', size })] })
    : new TextRun({ text: r.t, bold: !!r.b, size }));
}

function cell(children, width, shade) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: { top: none, bottom: none, left: none, right: none },
    shading: shade ? { type: ShadingType.CLEAR, color: 'auto', fill: shade } : undefined,
    margins: { top: 30, bottom: 30, left: 80, right: 80 }, children,
  });
}

function itemBlock(it, n) {
  const out = [];
  out.push(new Paragraph({
    heading: HeadingLevel.HEADING_3, keepNext: true,
    children: [new TextRun({ text: `${n}. ${it.title}` }), new TextRun({ text: `  ${it.date}`, bold: false, color: '666666' })],
  }));
  out.push(new Paragraph({ keepNext: true, spacing: { after: 80 }, children: [new TextRun(it.summary)] }));
  out.push(new Table({
    width: { size: TABLE_W, type: WidthType.DXA }, columnWidths: [LABEL_W, TABLE_W - LABEL_W], borders: noBorders,
    rows: it.rows.map(([label, runs]) => new TableRow({
      cantSplit: true,
      children: [
        cell([new Paragraph({ children: [new TextRun({ text: label, size: 18, color: '555555' })] })], LABEL_W, 'F2F2F2'),
        cell([new Paragraph({ children: textRuns(runs, 18) })], TABLE_W - LABEL_W),
      ],
    })),
  }));
  out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
  return out;
}

const body = [
  new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(P.title)] }),
  new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: P.subtitle, color: '555555' })] }),
  new Paragraph({ spacing: { after: 200 }, children: [
    new TextRun(P.intro + ' Site: '),
    new ExternalHyperlink({ link: P.site, children: [new TextRun({ text: P.site, style: 'Hyperlink' })] }),
  ] }),
];
let n = 0;
P.sections.forEach((s, i) => {
  body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: i > 0, children: [new TextRun(`${i + 1}. ${s.head}`)] }));
  body.push(new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: s.intro, italics: true })] }));
  s.items.forEach(it => body.push(...itemBlock(it, ++n)));
});
body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun('Left out on purpose')] }));
P.excluded.forEach(x => body.push(new Paragraph({
  numbering: { reference: 'bullets', level: 0 },
  children: [new TextRun({ text: x.slug, bold: true }), new TextRun(`: ${x.why}`)],
})));

const doc = new Document({
  creator: 'cyphersolver', title: P.title,
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { size: 40, bold: true, font: FONT }, paragraph: { spacing: { after: 80 } } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 30, bold: true, font: FONT }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 23, bold: true, font: FONT }, paragraph: { spacing: { before: 160, after: 40 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: 'bullets', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '888888' })] })] }) },
    children: body,
  }],
});

Packer.toBuffer(doc).then(buf => fs.writeFileSync(outPath, buf));
