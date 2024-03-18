const apiUrl = "https://api.openweathermap.org/data/2.5/weather"
const apiKey = "724950b777b31669fe8cbc0565c95a02"
const city = "Stockholm"
const url = `${apiUrl}?q=${city}&appid=${apiKey}&units=metric&lang=sv`;

function getWeatherFromApi(url) {
    fetch(url)
        .then(function(responseObject) {
            if (!responseObject.ok) {
                throw new Error("Det gick inte hitta sidan, se nätverksstatusen här: " + responseObject.status)
            }
            return responseObject.json()
        })
        .then(function(temp_data) {
            const temperature = temp_data.main.temp;
            // const location = temp_data.name;
            document.getElementById("weatherInfo").innerText = `The temperature where I am is currently ${temperature}°C`;
        })
        .catch(function(error) {
            console.error("något gick tyvärr fel se: " + error)
        })
}

getWeatherFromApi(url)


function addIconToWeather(url) {
    fetch(url)
        .then(function(responseObject) {
            if (!responseObject.ok) {
                throw new Error("Det gick inte hitta sidan, se nätverksstatusen här: " + responseObject.status)
            }
            return responseObject.json()
        })
        .then(function(weaterIcon) {
            const theIcon = weaterIcon.weather[0].main;

            const newElement = document.createElement("p");
            newElement.classList.add("weatherIcon");

            if (theIcon == "Clouds") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Cloudy.png"></img>';
            } else if (theIcon == "Clear") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Sunny.png"></img>';
            } else if (theIcon == "Atmosphere") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Atmosphere.png"></img>';
            } else if (theIcon == "Snow") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Snow.png"></img>';
            } else if (theIcon == "Rain") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Rain.png"></img>';
            } else if (theIcon == "Drizzle") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Drizzle.png"></img>';
            } else if (theIcon == "Thunderstorm") {
                newElement.innerHTML = '<img src="/images/weatherimgs/Thunderstorm.png"></img>';
            } else {
                newElement.innerHTML = "This would show an icon but cant fetch the image to show..";
            }
            document.getElementById("weatherInfo").appendChild(newElement);
        })
        .catch(function(error) {
            console.error("något gick tyvärr fel se: " + error)
        })
}

addIconToWeather(url)
