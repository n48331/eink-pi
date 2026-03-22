const { exec } = require("child_process");

function runDisplay(filePath) {
  return new Promise((resolve, reject) => {
    exec(`python3 ../python/convert.py ${filePath}`, (err, stdout, stderr) => {
      if (err) {
        console.error(stderr);
        return reject(err);
      }
      console.log(stdout);
      resolve();
    });
  });
}

module.exports = { runDisplay };
