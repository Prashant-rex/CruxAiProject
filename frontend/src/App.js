import React, { useState, useEffect } from 'react';
import './index.css'
import axios from 'axios';

const App = () => {
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [distance, setDistance] = useState('');
  const [loadingLocation, setLoadingLocation] = useState(true);
  const [foodTrucks, setFoodTrucks] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getUserLocation = () => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            setLatitude(position.coords.latitude.toFixed(6));
            setLongitude(position.coords.longitude.toFixed(6));
            setLoadingLocation(false);
          },
          (error) => {
            console.error('Error getting location:', error.message);
            setLoadingLocation(false);
          }
        );
      } else {
        console.error('Geolocation is not supported by your browser.');
        setLoadingLocation(false);
      }
    };

    getUserLocation();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const url = `http://localhost:8000/foodtrucks?lat=${latitude}&long=${longitude}&distance=${distance}`
      const response = await axios.get(url)
      setFoodTrucks(response.data)
    } catch (error) {
      setFoodTrucks([])
      setError('Something Went Wrong')
    }
  };

  return (
    <div className="location-form-container">
      <form onSubmit={handleSubmit} className="form">
        <div>
          <label>Latitude:</label>
          {loadingLocation ? (
            <input type="number" value="Loading..." readOnly />
          ) : (
            <input
              type="text"
              value={latitude}
              onChange={(e) => setLatitude(e.target.value)}
            />
          )}
        </div>
        <div>
          <label>Longitude:</label>
          {loadingLocation ? (
            <input type="number" value="Loading..." readOnly />
          ) : (
            <input
              type="number"
              value={longitude}
              onChange={(e) => setLongitude(e.target.value)}
            />
          )}
        </div>
        <div>
          <label>Distance (km):</label>
          <input
            type="number"
            value={distance}
            onChange={(e) => setDistance(e.target.value)}
          />
        </div>
        <button type="submit" disabled={latitude === '' || longitude === '' || distance === ''}>
          Submit
        </button>
      </form>

      {error && <p className="error-message">{error}</p>}

      <div className="food-trucks-list">
        {foodTrucks.map((truck, index) => (
          <div key={index} className="food-truck-box">
            <p className="food-truck-name">{truck.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
export default App;
