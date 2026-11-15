for n in $(seq 1 12); do
  c=$(curl -s -m 120 "http://web.archive.org/cdx/search/cdx?url=saassipa.cultura.gov.it/*&filter=mimetype:application/pdf&output=json&fl=original,timestamp,mimetype,length&collapse=urlkey" -o cdx_saassipa.json -w "%{http_code}")
  p=$(curl -s -m 30 -A "Mozilla/5.0 (research)" -o /dev/null -w "%{http_code}" https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/3941899)
  echo "$(date +%T) wb=$c pares=$p" >> poll.log
  [ "$c" = 200 ] && [ "$p" = 200 ] && break
  sleep 150
done
