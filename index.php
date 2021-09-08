<?php

require_once __DIR__ . '/vendor/autoload.php';

use GuzzleHttp\Client;

$instansi = $argv[1] ?? 'semarang';

$client = new Client([
    'base_uri' => 'https://data-sscasn.bkn.go.id',
    'timeout'  => 2.0,
]);

$found  = false;

do {
    try {
        $response = $client->get(
            '/ujian/list', [
            'query' => [
                'draw' =>	7,
                'columns[0][data]' =>	'instansi',
                'columns[0][name]' =>	'',
                'columns[0][searchable]' =>	true,
                'columns[0][orderable]' =>	true,
                'columns[0][search][value]' =>	'',
                'columns[0][search][regex]' =>	false,
                'columns[1][data]' =>	'jenis_pengadaan',
                'columns[1][name]' =>	'',
                'columns[1][searchable]' =>	true,
                'columns[1][orderable]' =>	true,
                'columns[1][search][value]' =>	'',
                'columns[1][search][regex]' =>	false,
                'columns[2][data]' =>	'titik_lokasi',
                'columns[2][name]' =>	'',
                'columns[2][searchable]' =>	true,
                'columns[2][orderable]' =>	true,
                'columns[2][search][value]' =>	'',
                'columns[2][search][regex]' =>	false,
                'columns[3][data]' =>	'alamat',
                'columns[3][name]' =>	'',
                'columns[3][searchable]' =>	true,
                'columns[3][orderable]' =>	true,
                'columns[3][search][value]' =>	'',
                'columns[3][search][regex]' =>	false,
                'columns[4][data]' =>	'mulai',
                'columns[4][name]' =>	'',
                'columns[4][searchable]' =>	true,
                'columns[4][orderable]' =>	true,
                'columns[4][search][value]' =>	'',
                'columns[4][search][regex]' =>	false,
                'columns[5][data]' =>	'selesai',
                'columns[5][name]' =>	'',
                'columns[5][searchable]' =>	true,
                'columns[5][orderable]' =>	true,
                'columns[5][search][value]' =>	'',
                'columns[5][search][regex]' =>	false,
                'order[0][column]' =>	0,
                'order[0][dir]' =>	'asc',
                'start' =>	0,
                'length' =>	10,
                'search[value]' =>	$instansi,
                'search[regex]' =>	false,
                '_' =>	time(),
            ]
        ]
        );
        $data = $response->getBody();
        $json = json_decode($data, true);
        
        if ($json['recordsTotal'] > 1) {
            print_r($json['data']);
            $found = true;
            break;
        }
        echo "Not found...\n";
        sleep(60 * 5);
        
    } catch (\Throwable $th) {
        echo "error\n";
    }
    
} while ($found == false);
