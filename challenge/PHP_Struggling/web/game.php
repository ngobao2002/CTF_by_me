<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/game.css"/>
    <title>Mini Blogs</title>
</head>
<body>
    <!-- Header -->
    <?php include 'header.php'; ?>

    <!-- Main -->
    <section class="new container" id="new">
        <!-- <div class="heading">
            <i class='bx bx-game'></i>
            <h2>Mini Blogs</h2>
        </div> -->

        <!-- Content -->
        <div class="mini-blogs">
            <!-- Mini Blog 1 -->
            <div class="mini-blog">
                <div class="mini-blog-title">
                    <h2>Level 1</h2>
                    <p>Introduction to the content of mini blog 1...</p>
                </div>
                <div class="mini-blog-content">
                    <p>This is the detailed content of mini blog 1. Here you can add more text, images, or any other content you want to include.</p>
                    <a href="../web/page/Level1/level1.php" class="play-btn">Play</a>
                </div>
            </div>

            <!-- Mini Blog 2 -->
            <div class="mini-blog">
                <div class="mini-blog-title">
                    <h2>Level 2</h2>
                    <p>Introduction to the content of mini blog 2...</p>
                </div>
                <div class="mini-blog-content">
                    <p>This is the detailed content of mini blog 2. Here you can add more text, images, or any other content you want to include.</p>
                    <a href="../web/page/Level2/level2.php" class="play-btn">Play</a>
                </div>
            </div>

            <!-- Add more mini blogs as needed -->
        </div>
    </section>

    <!-- JavaScript to handle content toggle -->
    <script>
        function toggleContent(blogId) {
            const content = document.getElementById(`content-${blogId}`);
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        }
    </script>
</body>
</html>
