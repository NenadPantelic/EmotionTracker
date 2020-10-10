import React from "react";

export default function Data(props) {
  const { url, email, title } = { props };
  return (
    <div className="data">
      <video width="300px" height="200px" src={url} controls />
      <h5>{email}</h5>
      <h5>{title}</h5>
    </div>
  );
}
