const express = require("express");
const uploadRoute = require("./routes/upload");
const path = require("path");

const app = express();

app.use(express.static(path.join(__dirname, "../frontend"))); // serve UI
app.use("/", uploadRoute);

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
