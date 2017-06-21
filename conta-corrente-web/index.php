<!DOCTYPE html>
<html>
<head>
	<title>Conta-Corrente</title>
	<style>
		form {
			margin: 2em 0;
		}
	</style>
</head>
<body>
<h1>Conta-Corrente</h1>
<p>Bem-vindo!</p>
<pre><?php
$address = "127.0.0.1";
$service_port = 7007;

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

$operacao = isset($_GET["operacao"]) && $_GET["operacao"] != "" ? $_GET["operacao"] : "SALDO";
$in = $operacao;
if ($operacao == "DEBITO" || $operacao == "CREDITO") {
	$valor = $_GET["valor"];
	$in .= " " . $valor;
}
$in .= "\n";
socket_write($socket, $in, strlen($in));

$out = socket_read($socket, 2048);

if ($operacao == "EXTRATO") {
	echo "EXTRATO: " . $out;
} else {
	echo "SALDO: " . $out;	
}

socket_close($socket);

?></pre>
<form action="." method="GET">
<input autofocus onfocus="this.select()" type="number" name="valor" value="0" />
<select name="operacao">
	<option value="">Selecione</option>
	<option value="CREDITO">Crédito</option>
	<option value="DEBITO">Débito</option>
</select>
<input type="submit" />
</form>
<form action="." method="GET">
<input type="submit" name="operacao" value="SALDO" />
<input type="submit" name="operacao" value="EXTRATO" />
</form>
</body>