<!DOCTYPE html>
<html>
<head>
	<title>Conta-Corrente</title>
</head>
<body>
<h1>Conta-Corrente</h1>
<p>Bem-vindo!</p>
<pre><?php
$address = "127.0.0.1";
$service_port = 6006;

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
// } else {
//     echo "OK.\n";
}

// echo "Attempting to connect to '$address' on port '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
// } else {
//     echo "OK.\n";
}

$in = "SALDO";
socket_write($socket, $in, strlen($in));

$out = socket_read($socket, 2048);

echo "SALDO: " . $out;

socket_close($socket);

?></pre>
</body>