import React, { useState } from "react";
import Header from "../components/Header";
import UploadBox from "../components/UploadBox";
import ResultCard from "../components/ResultCard";

function Home() {
  const [skills, setSkills] = useState([]);
  const [results, setResults] = useState([]);

  return (
    <div>
      <Header />
      <UploadBox setSkills={setSkills} setResults={setResults} />

      <div className="container mt-4">
        {skills.length > 0 && (
          <h5>Detected Skills: {skills.join(", ")}</h5>
        )}

        <div className="row">
          {results.map((item, index) => (
            <ResultCard key={index} data={item} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Home;