<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ZÉ AGROMÁQUINAS</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
}

body {
    background: #f5f2e9;
    color: #333;
}

header {
    background: #1b5e20;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 10px #0004;
}

nav {
    max-width: 1200px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    padding: 15px;
    align-items: center;
}

.logo {
    color: #ffc107;
    font-size: 28px;
    font-weight: bold;
}

nav ul {
    display: flex;
    list-style: none;
    gap: 25px;
}

nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.banner {
    height: 90vh;
    background: linear-gradient(#0008,#0008), url("banner.jpg");
    background-size: cover;
    background-position: center;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.banner h1 {
    font-size: 60px;
}

.banner p {
    color: #ffc107;
    font-size: 26px;
}

section {
    max-width: 1200px;
    margin: auto;
    padding: 80px 20px;
}

h2 {
    text-align: center;
    color: #1b5e20;
    margin-bottom: 30px;
    font-size: 38px;
}

.texto {
    text-align: center;
    line-height: 1.8;
    font-size: 18px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
    gap: 25px;
}

.card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 5px 15px #0003;
}

.card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}

.card div {
    padding: 20px;
}

.card h3 {
    color: #1b5e20;
    margin-bottom: 10px;
}

.botao {
    background: #2e7d32;
    color: white;
    padding: 12px 25px;
    display: inline-block;
    border-radius: 30px;
    text-decoration: none;
    margin-top: 15px;
    font-weight: bold;
}

.contato {
    text-align: center;
}

input, textarea {
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    border-radius: 8px;
    border: 1px solid #aaa;
}

form {
    max-width: 600px;
    margin: auto;
}

footer {
    background: #1b5e20;
    color: white;
    text-align: center;
    padding: 30px;
}

.whatsapp {
    position: fixed;
    right: 20px;
    bottom: 20px;
    background: #25d366;
    color: white;
    width: 60px;
    height: 60px;
    font-size: 30px;
    border-radius: 50%;
    text-align: center;
    line-height: 60px;
    text-decoration: none;
}

@media(max-width:700px){
    nav {
        flex-direction: column;
    }

    nav ul {
        margin-top: 10px;
        gap: 12px;
    }

    .banner h1 {
        font-size: 38px;
    }

    .banner p {
        font-size: 20px;
    }
}
</style>

</head>

<body>

<header>
<nav>
<div class="logo">🌽 ZÉ AGROMÁQUINAS</div>

<ul>
<li><a href="#quem">Quem Somos</a></li>
<li><a href="#servicos">Serviços</a></li>
<li><a href="#produtos">Produtos</a></li>
<li><a href="#contato">Contato</a></li>
</ul>

</nav>
</header>


<div class="banner">
<div>
<h1>ZÉ AGROMÁQUINAS</h1>
<p>Há mais de 40 anos cultivando confiança</p>
</div>
</div>


<section id="quem">
<h2>Quem Somos</h2>

<p class="texto">
A ZÉ AGROMÁQUINAS é uma empresa tradicional de Aragoiânia-GO,
com mais de quatro décadas atendendo produtores rurais com
compromisso, qualidade e confiança.
Nossa missão é oferecer produtos agrícolas de excelência e
um atendimento próximo ao homem do campo.
</p>

</section>


<section id="servicos">

<h2>Nossos Serviços</h2>

<div class="cards">

<div class="card">
<div>
<h3>🚜 Produção de Silagem</h3>
<p>Produção de silagem de alta qualidade para alimentação de bovinos de corte e leite.</p>
</div>
</div>

<div class="card">
<div>
<h3>🌾 Venda de Milho</h3>
<p>Fornecimento de milho a granel selecionado para diversas necessidades rurais.</p>
</div>
</div>

<div class="card">
<div>
<h3>🚚 Entrega na Região</h3>
<p>Atendimento rápido e entrega aos produtores rurais de toda a região.</p>
</div>
</div>

</div>

</section>


<section id="produtos">

<h2>Nossos Produtos</h2>

<div class="cards">

<div class="card">

<img src="silagem.jpg" alt="Silagem">

<div>
<h3>🌽 Silagem de Milho</h3>

<p>
Silagem produzida com alto padrão de qualidade,
garantindo melhor nutrição e desempenho do rebanho.
</p>

<a class="botao" href="https://wa.me/556299517635">
Solicitar orçamento
</a>

</div>

</div>


<div class="card">

<img src="milho.jpg" alt="Milho">

<div>

<h3>🌾 Milho a Granel</h3>

<p>
Milho selecionado e armazenado corretamente para oferecer qualidade ao produtor.
</p>

<a class="botao" href="https://wa.me/556299517635">
Solicitar orçamento
</a>

</div>

</div>

</div>

</section>


<section id="contato">

<h2>Entre em Contato</h2>

<div class="contato">

<p><strong>📍 Aragoiânia - GO</strong></p>
<p><strong>📞 WhatsApp:</strong> (62) 99517-635</p>
<p><strong>📸 Instagram:</strong> @ze_agromaquinas</p>

<br>

<form>

<input type="text" placeholder="Seu nome">

<input type="tel" placeholder="Telefone">

<textarea rows="5" placeholder="Digite sua mensagem"></textarea>

<a class="botao" href="https://wa.me/556299517635">
Enviar pelo WhatsApp
</a>

</form>

</div>

</section>


<footer>

<h3>🌽 ZÉ AGROMÁQUINAS</h3>

<p>
Há mais de 40 anos cultivando confiança no campo.
</p>

<p>
Atendemos Aragoiânia e toda a região.
</p>

</footer>


<a class="whatsapp"
href="https://wa.me/556299517635">
📱
</a>


</body>

</html>
