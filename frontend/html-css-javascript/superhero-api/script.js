// Superhero api
// Tyler Dinn

// API URL and Token
const SUPERHERO_TOKEN = "10166257269910585";
const BASE_URL = `https://superheroapi.com/api.php/${SUPERHERO_TOKEN}`;

const superheroBtn = document.getElementById("superhero-btn");
const heroImg = document.getElementById("hero-img");
const heroSearchBtn = document.getElementById("hero-search-btn");
const heroSearch = document.getElementById("hero-search");

const getSearchedSuperhero = (name) => {
  fetch(`${BASE_URL}/search/${name}`)
    .then((response) => response.json())
    .then((json) => {
      const hero = json.results[0];
      showHeroInfo(hero);
    });
};

const getSuperHero = (id) => {
  fetch(`${BASE_URL}/${id}`)
    .then((response) => response.json())
    .then((json) => {
      showHeroInfo(json);
    });
};

const statToEmoji = {
  intelligence: "🧠",
  strength: "💪",
  speed: "⚡️",
  durability: "🏋️",
  power: "🔋",
  combat: "🤺",
};

const showHeroInfo = (character) => {
  const name = `<h2>${character.name}</h2>`;
  const img = `<img src="${character.image.url}" height= 500px width= 500px/>`;

  const stats = Object.keys(character.powerstats)
    .map((stat) => {
      return `<p>${statToEmoji[stat]} ${stat.toUpperCase()}: ${
        character.powerstats[stat]
      }</p>`;
    })
    .join("");

  heroImg.innerHTML = `${name}${img}${stats}`;
};

const randomHero = () => {
  const numbeOfHeros = 731;
  return Math.floor(Math.random() * numbeOfHeros + 1);
};

superheroBtn.onclick = () => getSuperHero(randomHero());
heroSearchBtn.onclick = () => getSearchedSuperhero(heroSearch.value);
