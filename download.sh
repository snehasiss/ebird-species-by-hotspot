#!bash

if [ "x$1" == "x" ] || [ "x$2" == "x" ]; then
	echo "usage: bash $0 CODE NAME"
	echo "       CODE: eBird hotspot location code"
	echo "       NAME: any suitable location name"
	exit
fi

# constants
CODE=$1
LOCATION="${1}-${2}"

BINDIR="bin"
DATADIR="data"

SCRIPT="html-csv.py"
WGET="wget -qO "
URL="http://ebird.org/ebird/printableList?regionCode=${CODE}&yr=all&m="

# clear any previous download
rm -f ${DATADIR}/${LOCATION}.{html,csv}

# download printable html
${WGET} ${DATADIR}/${LOCATION}.html $URL

# create csv from html
python ${BINDIR}/${SCRIPT} ${DATADIR}/${LOCATION}.html > ${DATADIR}/${LOCATION}.csv
rm -f ${DATADIR}/${LOCATION}.html
