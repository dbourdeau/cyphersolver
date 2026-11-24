(() => {
  const board = document.querySelector(".cipher-board");
  const rows = Array.from(board.querySelectorAll(".cipher-row"), row =>
    Array.from(row.querySelectorAll(".cipher-cell"))
  );
  const section = document.querySelector("#section");
  const step = document.querySelector("#step");
  const result = document.querySelector("#position");
  const symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@";
  const letters = "ulhieeektdlnltcoytsevnddteaowfasheopartehhneileamishgraeobnftir";
  let previous;
  function update() {
    const block = section.selectedIndex;
    const i = Number(step.value) - 1;
    let row, column;
    if (block === 2) {
      row = 19 - Math.floor(i / 17);
      column = 16 - i % 17;
    } else {
      const height = block === 0 ? 10 : 8;
      row = (block === 0 ? 0 : 10) + (height - i % height) % height;
      column = i * (block + 1) % 17;
      // Show the cell on the printed sheet, before reversing the copying slip.
      if (row === 13 && column >= 4) column = column === 4 ? 16 : column - 1;
    }
    if (previous) previous.classList.remove("picked");
    previous = rows[row][column];
    previous.classList.add("picked");
    const symbol = previous.textContent;
    const letter = letters[symbols.indexOf(symbol)].toUpperCase();
    result.textContent = "Step " + (i+1) + " · row " + (row+1) + ", column " + (column+1) + " · " + symbol + " → " + letter;
  }
  section.addEventListener("change", () => {
    step.max = [170,136,34][section.selectedIndex];
    step.value = 1;
    update();
  });
  step.addEventListener("input", update);
  document.querySelector(".route-controls").hidden = false;
  update();
})();
