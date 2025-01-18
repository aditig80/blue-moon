// XOR encoding to obfuscate the flag
function xorEncode(text, key) {
    var result = '';
    for (var i = 0; i < text.length; i++) {
        result += String.fromCharCode(text.charCodeAt(i) ^ key);
    }
    return result;
}

// Function to decode the encoded flag
function getFlag() {
    // The correctly Base64-encoded full flag
    var encodedFlag = "ZmxhZ0NFU3t5b3VfYXJlX2Zvb2xlZA=="; // Base64 for "flagCES{you_are_fooled}"

    // Decode the Base64-encoded flag
    var decodedFlag = atob(encodedFlag);

    // Apply XOR encoding to further obscure the flag
    var key = 27;  // XOR key
    var encodedFlagWithXOR = xorEncode(decodedFlag, key);  // Further encode with XOR

    return encodedFlagWithXOR;
}

// Simulate some random processing
function simulateProcessing() {
    for (var i = 0; i < 1000000; i++) {
        Math.sqrt(i);  // Doing some heavy operations
    }
}

// A function to simulate waiting time
function fakeDelay() {
    var start = Date.now();
    while (Date.now() - start < 3000) {
        // Fake delay of 3 seconds
    }
}

// Final function to decode and show the flag
function revealFlag() {
    var encodedFlag = getFlag();
    
    // Simulate a delay and processing before revealing the flag
    fakeDelay();
    simulateProcessing();
    
    // Decrypt flag using XOR decoding
    var decryptedFlag = xorEncode(encodedFlag, 27);
    
    // Show the decoded flag
    document.getElementById("result").innerHTML = decryptedFlag;
}

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Hide the login form
    document.getElementById("loginForm").style.display = "none";
    
    // Perform some complex operations before revealing the flag
    revealFlag();
});
