document.getElementById('checkButton').addEventListener('click', function() {
    const snoringCount = parseInt(document.getElementById('snoringCount').value);
    const resultDiv = document.getElementById('result');

    if (isNaN(snoringCount) || snoringCount < 0) {
        resultDiv.textContent = 'Please enter a valid snoring count.';
        resultDiv.style.color = 'red'; 
        return;
    }

    let message = '';

    if (snoringCount >= 30) {
        message = 'High snoring count detected! You might be at risk for obstructive sleep apnea.';
        message += '<br>" Consult Your Doctor Immediately " ';
        message += '<br>';
        message += '<ul style="list-style-position: inside; margin: 0; padding-left: 20px;">'; 
        message += '<li>Use prescribed medicines on time .</li>';
        message += '<li>Monitor your snoring count with SNOR-O-CARDIO.</li>';
        message += '<li>Be far from Dusty places</li>';
        message += '<li>Avoid alcohol and sedatives before bedtime.</li>';
        message += '</ul>';
        resultDiv.style.color = 'orange'; 
    }
        else if(snoringCount>=5 & snoringCount<15){
            message ='  your snoring problem have just started ,you have to be careful and Follow a healthy lifestyle';
            message =' Monitor your snoring count with SNOR-O-CARDIO.';
            resultDiv.style.color = 'green'; 
        }
        else if(snoringCount>=15 & snoringCount<30){
            message =' Please be careful... You may enter into high risk stage' ;
            message += '<br>Here are some home remedies you can try:';
            message += '<br>';
            message += '<ul style="list-style-position: inside; margin: 0; padding-left: 20px;">'; 
            message += '<li>Practice Yoga to help with relaxation and breathing.</li>';
            message += '<li>Maintain a healthy weight.</li>';
            message += '<li>Sleep on your side.</li>';
            message += '<li>Avoid alcohol and sedatives before bedtime.</li>';
            message += '<li>Stay hydrated.</li>';
            message += '</ul>';
              resultDiv.style.color = 'green'; 
        }
    else {
        message = 'Your snoring count is within a normal range. However, maintaining good sleep hygiene is always recommended.';
        resultDiv.style.color = 'green'; 
    }

    resultDiv.innerHTML = message;
});
