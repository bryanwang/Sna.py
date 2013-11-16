<html>
<head>
	<link rel="stylesheet" type="text/css" href="/snapy/style"/>
  	<link rel="stylesheet" type="text/css" href="/snapy/theme"/>
	<style type="text/css">
      body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
      }

      .table-rows {
        padding: 19px 29px 29px;
        margin: 0 auto 20px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
        -webkit-border-radius: 5px;
           -moz-border-radius: 5px;
                border-radius: 5px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.05);
           -moz-box-shadow: 0 1px 2px rgba(0,0,0,.05);
                box-shadow: 0 1px 2px rgba(0,0,0,.05);
      }

    </style>
</head>
<body>
	<div class='container' id='snapchats'>
		<table class='table table-hover table-rows' border="1">
			<thead>
				<tr>
					%for d in snap:
						<th>{{d}}</th>
					%end
				</tr>
			</thead>
			%for s in snaps:
				<tbody>
					<tr>
					%for d in s:
						<td>{{s[d]}}</td>
					%end
					</tr>
				</tbody>
			%end
		</table>
	</div>	
</body>
</html>