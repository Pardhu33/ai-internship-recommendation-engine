import React, { useState } from "react";

function ResultCard({ data }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="col-md-4 mt-4">
      <div
        className="card p-3 shadow-sm card-hover"
        onClick={() => setOpen(!open)}
      >
        <h5>{data.title}</h5>
        <p><b>Company:</b> {data.company}</p>
        <p className="text-success"><b>Match:</b> {data.match}%</p>

        {open && (
          <div className="mt-3">
            <p><b>Location:</b> {data.location}</p>
            <p>{data.description}</p>

            <a
              href={data.link}
              target="_blank"
              rel="noreferrer"
              className="btn btn-primary btn-sm"
            >
              Apply Now
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default ResultCard;