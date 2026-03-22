const express = require("express");
const multer = require("multer");
const { runDisplay } = require("../services/displayService");

const router = express.Router();

const upload = multer({ dest: "uploads/" });

router.post("/upload", upload.single("image"), async (req, res) => {
 console.log("UPLOAD HIT 🚀");
  try {
    await runDisplay(req.file.path);
    res.send("Displayed on E-Ink ✅");
  } catch (err) {
    res.status(500).send("Error processing image");
  }
});

module.exports = router;
