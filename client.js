<script>
 
    const socket = new WebSocket('ws://localhost:5000');
 
socket.addEventListener('open', function (event) {
 
    socket.send('Connection Established');
 
});
