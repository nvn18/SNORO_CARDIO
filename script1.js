const startButton = document.getElementById('start-button');
const statusElement = document.getElementById('status');

let audioContext;
let analyzer;

async function startDetection() {
    try {
        // Request access to the microphone
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const source = audioContext.createMediaStreamSource(stream);
        
        // Create analyzer node
        analyzer = audioContext.createAnalyser();
        analyzer.fftSize = 2048;
        source.connect(analyzer);
        
        statusElement.textContent = "Listening for snoring...";
        monitorAudio();
    } catch (err) {
        console.error('Error accessing microphone:', err);
        statusElement.textContent = "Error accessing microphone.";
    }
}

function monitorAudio() {
    const dataArray = new Uint8Array(analyzer.frequencyBinCount);
    
    function analyze() {
        analyzer.getByteFrequencyData(dataArray);
        
        // Calculate the average volume
        const avgVolume = dataArray.reduce((sum, value) => sum + value, 0) / dataArray.length;

        // Detect snoring based on volume threshold
        if (avgVolume > 100) { // Adjust threshold as needed
            statusElement.textContent = "Snoring detected!";
            statusElement.classList.add('snore-detected');
        } else {
            statusElement.textContent = "No snoring detected.";
            statusElement.classList.remove('snore-detected');
        }
        
        requestAnimationFrame(analyze);
    }
    
    analyze();
}

startButton.addEventListener('click', startDetection);
