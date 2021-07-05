<?php
<html>
	<head>
		<style>
			#body {box-sizing: border-box;
			       font-style: sans-serif;
			}
				#huh {
				margin-top: 10px;
				text-align: center;
				}
				
				#fm {
				margin-top: 40px;
				width: 100px;
				margin-left: 40%;
				}
				spam {margin-left: 5px;}
				#sub {
				border: 0px;
				border-radius: 15px;
				background: transparent;
				color: black;
				transition: 0.5s;
				}
				#sub:hover, #sub:active {
				background: cyan;
				color: white;
				font-style: sans-serif;
				}
			</style>
		</head>
		<body>
			<h1 id="huh">Trying. Deployed on heroku</h1>
			<form id="fm" action="post.php" method="POST">
				<span id="nnn">Name -</span><input type="txt" id="name" placeholder="Name" required></input>
				<span id="pssd">Password - <input type="password" id="psd" placeholder="Password" required></input>
				<input id="sub" type="submit">Submit</input>
				</form>
			</body>
			</html>
			?>