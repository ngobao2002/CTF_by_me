<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/login.css">
    <title>Register page</title>
</head>
<body>
    <!-- <p>Account admin: admin/999</p> -->
    <div class="main">
        <h1>LOGIN TO FIND FLAG</h1>
        <h3>Register in here</h3>
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

            <label for="password">
                Password:
            </label>
            <input type="password"
                    id="password"
                    name="password"
                    placeholder="Enter your password again" required>

            <div class="wrap">
                    <button type="submit"
                            onclick="solve()">
                        Submit
                    </button>
            </div>
        </form>
        <p>You have account already?
            <a href="#"
                style="text-decoration: none;">
                    Login in here
            </a>
        </p>
    </div>
</body>
</html>