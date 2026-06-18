import React, { useState } from "react";

function UploadBox({ setSkills, setResults }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setSkills(data.skills);
    setResults(data.recommendations);
  };

  return (
    <div className="text-center mt-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />
      <button className="btn btn-primary mt-3" onClick={handleUpload}>
        Upload Resume
      </button>
    </div>
  );
}

export default UploadBox;