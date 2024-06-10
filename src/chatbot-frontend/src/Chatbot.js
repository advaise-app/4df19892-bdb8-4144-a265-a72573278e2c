import React, { useState } from "react";
import axios from "axios";
import "./Chatbot.css";

export default function Chatbot() {
  // State variables to store the user query, role, experience, employment type, and answer
  const [query, setQuery] = useState("");
  const [role, setRole] = useState("");
  const [experience, setExperience] = useState("");
  const [employmentType, setEmploymentType] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  // Event handler to update the query state variable
  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSearchSubmit = async (e) => {
    e.preventDefault();
    await fetchAnswer(query);
  };

  const handleFilterSubmit = async (e) => {
    e.preventDefault();
    const question = buildQuery();
    await fetchAnswer(question);
  };

  // Function to build the query based on the role, experience, and employment type
  const buildQuery = () => {
    let query = "Find people who fulfil the following requirements:";
    if (role) query += ` they are a ${role}`;
    if (experience) query += `, they have ${experience} years of experience`;
    if (employmentType) query += `, they are a ${employmentType}`;
    if (!role && !experience && !employmentType) query += " any person";
    return query;
  };

  // Function to fetch the answer from the Rest API
  const fetchAnswer = async (question) => {
    setAnswer("");
    setLoading(true);
    try {
      const API_BASE_URL = "http://localhost:8000";
      const response = await axios.post(`${API_BASE_URL}/api/answer/`, {
        query: question,
      });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error("Error:", error);
    }
    setLoading(false);
  };

  // JSX to render the chatbot UI
  return (
    <div className="chatbot-container">
      {/* Add the logo and subtitle */}
      <div className="chatbot-logo">AI Chatbot</div>
      <div className="chatbot-subtitle">
        Ask me about people working at DemoCo
      </div>

      {/* Add the form to input the query */}
      <form className="chatbot-form" onSubmit={handleSearchSubmit}>
        <div className="chatbot-input-container">
          <input
            type="text"
            value={query}
            onChange={handleQueryChange}
            placeholder="Enter your query"
            className="chatbot-input"
          />
          <button type="submit" className="chatbot-button">
            Search
          </button>
        </div>
      </form>

      {/* Question builder */}
      <div className="chatbot-question-builder">
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="">Select a role</option>
          <option value="project manager">Project Manager</option>
          <option value="diversity and inclusiveness researcher">
            Diversity and Inclusiveness Researcher
          </option>
        </select>

        {/* Experience and Employment type select */}
        <select
          value={experience}
          onChange={(e) => setExperience(e.target.value)}
        >
          <option value="">Select experience</option>
          <option value="more than 15">More than 15 years</option>
          <option value="less than 15">Less than 15 years</option>
        </select>
        <select
          value={employmentType}
          onChange={(e) => setEmploymentType(e.target.value)}
        >
          <option value="">Select employment type</option>
          <option value="contractor">Contractor</option>
          <option value="permanent">Permanent</option>
        </select>
        <button onClick={handleFilterSubmit} className="chatbot-button">
          Filter
        </button>
      </div>

      {/* Question preview */}
      <div className="chatbot-question-preview">{buildQuery()}</div>

      {/* Display the loading text */}
      {loading && <div className="chatbot-loading">Loading...</div>}

      {/* Display the answer */}
      {answer && (
        <div className="chatbot-result">
          <p className="answer">{answer}</p>
        </div>
      )}
    </div>
  );
}