import React, { useState } from "react";
import axios from "axios";
import "./Chatbot.css";

export default function Chatbot() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [showSuggestions, setShowSuggestions] = useState(true);

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setShowSuggestions(false);
    await fetchAnswer(query);
  };

  const handleSuggestionClick = async (suggestion) => {
    setQuery(suggestion);
    setShowSuggestions(false);
    await fetchAnswer(suggestion);
  };
  
  const fetchAnswer = async (question) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/answer/', { query: question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const suggestions = [
    'Find people who fulfill the following requirements: any person',
    'Find people who fulfill the following requirements: they are a project manager',
    'Find people who fulfil the following requirements: they are a project manager, they have more than 15 years of experience',
    // Add more suggested questions as needed
  ];

  return (
    <div className="chatbot-container">
      <div className="chatbot-logo">AI Chatbot</div>
      <div className="chatbot-subtitle">Ask me about people working at DemoCo</div>
      <form className="chatbot-form" onSubmit={handleSubmit}>
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
      {showSuggestions && (
        <div className="chatbot-suggestions">
          {suggestions.map((suggestion, index) => (
            <div
              key={index}
              className="chatbot-suggestion"
              onClick={() => handleSuggestionClick(suggestion)}
            >
              {suggestion}
            </div>
          ))}
        </div>
      )}
      {answer && (
        <div className="chatbot-result">
          <p className="answer">{answer}</p>
        </div>
      )}
    </div>
  );
}
