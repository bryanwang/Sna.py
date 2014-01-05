<html>
<head>
	<link rel="stylesheet" type="text/css" href="/snapy/style"/>
  <link rel="stylesheet" type="text/css" href="/snapy/theme"/>
  <meta name="viewport" content="width=320" />
  <meta name="viewport" content="user-scalable=no" />
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
		<div class='container'>
				<ul class='list-group' border="1">
          %for i in range(0, len(ids)):
  					<li id='item' class='list-group-item'>
              <button id='viewbutton' type='submit' class='btn btn-sm btn-primary' onClick="window.location={{loadImage[i]}}">View</button>
  						<b>From: <i>{{senders[i]}}</i></b>
  					</li>
          %end
				</ul>
		</div>
</body>
</html>