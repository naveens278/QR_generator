function generateQR() {
    let text = document.getElementById("qrText").value;
    let qrContainer = document.getElementById("qrcode");
    let qrSection = document.querySelector(".qr-section");

    if (text === "") {
        alert("Please enter some text!");
        return;
    }

    // Clear previous QR code
    qrContainer.innerHTML = "";

    let qr = new QRCode(qrContainer, {
        text: text,
        width: 200,
        height: 200
    });

    // Show QR section with animation
    setTimeout(() => {
        qrSection.classList.add("show");
        document.getElementById("downloadBtn").style.display = "block";
    }, 200);
}

function downloadQR() {
    let qrCanvas = document.querySelector("#qrcode canvas");
    let qrImage = qrCanvas.toDataURL("image/png");

    let link = document.createElement("a");
    link.href = qrImage;
    link.download = "QR_Code.png";
    link.click();
}
