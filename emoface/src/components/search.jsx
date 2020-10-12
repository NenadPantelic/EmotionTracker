import React, { useState } from "react";
import { Link } from "react-router-dom";
import Data from "./data";

const result = [
  {
    id: 1,
    first_name: "Carrissa",
    last_name: "Mepham",
    email: "cmepham0@guardian.co.uk",
    title: "Female",
    ip_address: "88.236.211.106",
    url: "https://www.youtube.com/watch?v=s66w28knp80",
  },
  {
    id: 2,
    first_name: "Darius",
    last_name: "Pitchers",
    email: "dpitchers1@moonfruit.com",
    title: "Male",
    ip_address: "95.36.49.244",
    url: "https://www.youtube.com/watch?v=s66w28knp80",
  },
  {
    id: 3,
    first_name: "Norbert",
    last_name: "Nesbit",
    email: "nnesbit2@cbslocal.com",
    title: "Male",
    ip_address: "38.25.33.44",
    url: "https://www.youtube.com/watch?v=s66w28knp80",
  },
];

export default function Search() {
  const [info, setInfo] = useState(result);

  const handleSearch = (e) => {
    e.preventDefault();

    const url = document.getElementById("url");
    fetch(url)
      .then((res) => {
        // setInfo(result);
        console.log(info);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="search-wrapper">
      <form>
        <input
          className="input"
          type="text"
          name="url"
          id="url"
          placeholder="Enter Url Here"
        />
        <input
          className="submit"
          onClick={handleSearch}
          type="submit"
          value="Search"
        />
      </form>
      <div className="result-container">
        {info && info.map((item) => <Data {...item} />)}
      </div>

      <Link to="/dashboard">{"<< Back"}</Link>
    </div>
  );
}
