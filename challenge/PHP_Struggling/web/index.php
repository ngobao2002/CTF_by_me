<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/style.css"/>
    <title>Document</title>
</head>
<body>
    <?php include 'header.php'; ?>
    <section class="hero-section">
        <div class="hero">
            <h2>LLM Jalibreak CTF</h2>
            <p>   
                This is the CTF website of Tâm Anh and Tâm Bảo. 
                We have created a CTF playground where you can explore logical flaws and, especially, 
                the LLM Jailbreak challenge. 
                Join our game and have a fun experience!
            </p>
            <div class="buttons">
                <a href="#" class="join">Play Now</a>
                <a href="#" class="learn" onclick="showRules()">Read More</a>
            </div>
        </div>
        <div class="img">
            <img src="../image/hero-bg.png" alt="hero image" />
        </div>
    </section>
    <!-- Popup Modal -->
    <div id="rulesModal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeRules()">&times;</span>
            <h2>Game Rules</h2>
            <p>Here are the rules for the CTF game...</p>
            Welcome to our CTF website! This is where you'll experience a series of unique and exciting challenges. 
            In this CTF world, you'll need to use your skills and intelligence to find two hidden flags on the website and our bot.
            Your goal is to collect enough point to use our special chatbot. 
            This chatbot is not just an ordinary communication tool; it also contains special challenges related to LLM Jailbreak – one of the most exciting parts of this game. 
            Once you own the chatbot, you'll have the opportunity to explore and interact with it, discovering weaknesses, logical flaws, and opportunities to overcome the barriers set by the game creators.
        </div>
    </div>
</body>
<script>
    function showRules() {
        document.getElementById('rulesModal').style.display = 'block';
    }

    function closeRules() {
        document.getElementById('rulesModal').style.display = 'none';
    }

    // Close the modal when clicking outside of it
    window.onclick = function(event) {
        var modal = document.getElementById('rulesModal');
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
</script>
</html>