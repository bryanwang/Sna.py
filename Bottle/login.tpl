<html>
{% block head %}
	<style type="text/css">
      body {
              padding-top: 40px;
              padding-bottom: 40px;
              background-color: #eee;
            }

            .form-signin {
              max-width: 330px;
              padding: 15px;
              margin: 0 auto;
            }
            .form-signin .form-signin-heading,
            .form-signin .checkbox {
              margin-bottom: 10px;
            }
            .form-signin .checkbox {
              font-weight: normal;
            }
            .form-signin .form-control {
              position: relative;
              font-size: 16px;
              height: auto;
              padding: 10px;
              -webkit-box-sizing: border-box;
                 -moz-box-sizing: border-box;
                      box-sizing: border-box;
            }
            .form-signin .form-control:focus {
              z-index: 2;
            }
            .top-cap {
              margin-bottom: -1px;
              border-bottom-left-radius: 0;
              border-bottom-right-radius: 0;
            }
            .middle-plug {
              margin-bottom: -1px;
              border-top-left-radius: 0;
              border-top-right-radius: 0;
              border-bottom-left-radius: 0;
              border-bottom-right-radius: 0;
            }
            .bottom-cap {
              margin-bottom: 10px;
              border-top-left-radius: 0;
              border-top-right-radius: 0;
            }
    </style>
{% endblock %}
<body>
	<div class='container' id='auth'>
		<form class='form-signin' action='/snapy/web_login' method='POST'>
			<h2 class='form-signin-heading'>Please sign in</h2>
			<input class='form-control top-cap' type='text' name='username' placeholder='username' required autofocus/>
      <input class='form-control bottom-cap' type='password' name='password' placeholder='password' required/><br />
			<button type='submit' class='btn btn-lg btn-primary'>Login</button><br />
      <br /><a href='/snapy/web_signup'>Don't have an account?</a>		</form>
  </div>
  <div class='container' id='auth'>
    <form class='form-signin' action='/snapy/web_send' method='POST'>
      <h2 class='form-signin-heading'>Send image (.jpg only)</h2>
      <input class='form-control top-cap' type='text' name='username' placeholder='username' required autofocus/>
      <input class='form-control middle-plug' type='password' name='password' placeholder='password' required/>
      <input class='form-control middle-plug' type='text' name='recipient' placeholder='recipient' required/>
      <input class='form-control bottom-cap' type='file' name='data' required/><br />
      <button type='submit' class='btn btn-lg btn-primary'>Send</button></form>
  </div>
</body>
</html>