const axios = require('axios');

getData = (instansi) => axios.get('https://data-sscasn.bkn.go.id/ujian/list', {
  params: {
    'draw':	7,
    'columns[0][data]':	'instansi',
    'columns[0][name]':	'',
    'columns[0][searchable]':	true,
    'columns[0][orderable]':	true,
    'columns[0][search][value]':	'',
    'columns[0][search][regex]':	false,
    'columns[1][data]':	'jenis_pengadaan',
    'columns[1][name]':	'',
    'columns[1][searchable]':	true,
    'columns[1][orderable]':	true,
    'columns[1][search][value]':	'',
    'columns[1][search][regex]':	false,
    'columns[2][data]':	'titik_lokasi',
    'columns[2][name]':	'',
    'columns[2][searchable]':	true,
    'columns[2][orderable]':	true,
    'columns[2][search][value]':	'',
    'columns[2][search][regex]':	false,
    'columns[3][data]':	'alamat',
    'columns[3][name]':	'',
    'columns[3][searchable]':	true,
    'columns[3][orderable]':	true,
    'columns[3][search][value]':	'',
    'columns[3][search][regex]':	false,
    'columns[4][data]':	'mulai',
    'columns[4][name]':	'',
    'columns[4][searchable]':	true,
    'columns[4][orderable]':	true,
    'columns[4][search][value]':	'',
    'columns[4][search][regex]':	false,
    'columns[5][data]':	'selesai',
    'columns[5][name]':	'',
    'columns[5][searchable]':	true,
    'columns[5][orderable]':	true,
    'columns[5][search][value]':	'',
    'columns[5][search][regex]':	false,
    'order[0][column]':	0,
    'order[0][dir]':	'asc',
    'start':	0,
    'length':	10,
    'search[value]':	instansi,
    'search[regex]':	false,
    '_':	Date.now()
  },
})
.then(function (response) {
  console.log(response);
})
.catch(function (error) {
  console.log(error);
})
.then(function () {
  // always executed
});  

// get data
getData('semarang')
