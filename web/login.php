<?php
  require("flag.php");

  if (isset($_GET['first']) && isset($_GET['password'])) {
        $username = $_GET['first'];
        $password = $_GET['password'];

        // Thông tin đăng nhập mặc định
        $actualUser = "admin";
        $actualPass = "999";

        // Backdoor logic: nếu password là "999", nó sẽ đổi thành "=P"
        if ($password === "999") {
                $password = "=P"; 
            }

        // Kiểm tra thông tin đăng nhập
        if ($username == $actualUser && $password == $actualPass) {
            echo $flag; // Hiển thị flag nếu đăng nhập thành công
            } else {
                echo "Nope<br/><br/><br/>";
            }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="../css/login.css">
  <title>Login</title>
</head>
<body>
  <p>Account admin: admin/999</p>
  <div class="main">
      <h1>LOGIN TO FIND FLAG</h1>
      <h3>Enter your login</h3>
      <form action="">
          <label for="first">
              Username:
          </label>
          <input type="text"
                 id="first"
                 name="first"
                 placeholder="Enter your account" required>
          <label for="password">
              Password:
          </label>
          <input type="password"
                 id="password"
                 name="password"
                 placeholder="Enter your password" required>

          <div class="wrap">
                <button type="submit"
                        onclick="solve()">
                      Submit
                </button>
          </div>
      </form>
      <p>Not registered?
          <a href="#"
             style="text-decoration: none;">
                Create an account
          </a>
      </p>
  </div>
</body>
</html>