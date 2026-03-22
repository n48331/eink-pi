let cropper = null;

const input = document.getElementById("inputImage");
const image = document.getElementById("image");

// Handle image selection
input.addEventListener("change", function (e) {
  const file = e.target.files[0];

  if (!file) return;

  const url = URL.createObjectURL(file);

  // Destroy previous cropper instance
  if (cropper) {
    cropper.destroy();
    cropper = null;
  }

  image.src = url;

  // Wait for image to load before initializing cropper
  image.onload = () => {
    cropper = new Cropper(image, {
      aspectRatio: 212 / 104, // match your e-ink display
      viewMode: 1,
      autoCropArea: 1,
      responsive: true,
      background: false,
    });
  };
});

// Upload function
function upload() {
  if (!cropper) {
    alert("Please select and crop an image first");
    return;
  }

  const canvas = cropper.getCroppedCanvas({
    width: 212,
    height: 104,
  });

  if (!canvas) {
    alert("Crop failed. Try again.");
    return;
  }

  canvas.toBlob((blob) => {
    if (!blob) {
      alert("Image conversion failed");
      return;
    }

    const formData = new FormData();
    formData.append("image", blob, "cropped.png");

    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.text())
      .then((data) => {
        alert(data);
        console.log("Server response:", data);
      })
      .catch((err) => {
        console.error("Upload error:", err);
        alert("Upload failed");
      });
  }, "image/png");
}
