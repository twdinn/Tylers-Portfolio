// open weather map api
// Tyler Dinn

// API Key
const API_KEY = "424cb45f603168c74d854972abb8d026";

// Get Elements
let search = document.getElementById("search");
let cityNameDIv = document.getElementById("city-name");
let weatherTypeDiv = document.getElementById("weather-type");
let tempDiv = document.getElementById("temp");
let maxTempDiv = document.getElementById("max-temp");
let minTempDiv = document.getElementById("min-temp");
let searchBtn = document.getElementById("search-btn");

// Pull in data from open weather map api
// City = what the user type in
const getSearchedWeather = async (city) => {
  city = search.value;
  let response = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`
  );
  let json = await response.json();

  displayWeather(json);
};

// Display data need in the DOM
const displayWeather = (json) => {
  const weatherType = json.weather[0].description.toUpperCase();
  const city = search.value;
  const temp = `Temp: ${json.main.temp}°C`;
  const maxTemp = `Max Temp: ${json.main.temp_max}°C`;
  const minTemp = `Min Temp: ${json.main.temp_min}°C`;

  cityNameDIv.innerHTML = city;
  weatherTypeDiv.innerHTML = weatherType;
  tempDiv.innerHTML = temp;
  maxTempDiv.innerHTML = maxTemp;
  minTempDiv.innerHTML = minTemp;
};

searchBtn.onclick = () => getSearchedWeather();
