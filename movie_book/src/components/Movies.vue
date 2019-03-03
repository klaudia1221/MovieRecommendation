<template>
  <div class="hello">
    <h1>Movie Recommendation</h1>

    <div class="favs cards">

<card v-for="m in movies" :key="m.id"
:title="m.title"
:description="m.year"
:img="m.img"
 />

    </div>

    <div class="movies cards">

<card v-for="m in movies" :key="m.id"
:title="m.title"
:description="m.year"
:img="m.img"
 />
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      movies: [
        {
          'id': 1,
          'title': 'Titanic',
          'year': 1997,
          'prob': 0.9,
          'img': 'https://images-na.ssl-images-amazon.com/images/I/51gEpO63aRL.jpg'
        },
        {
          'id': 2,
          'title': 'Titanic',
          'year': 1997,
          'prob': 0.9,
          'img': 'https://images-na.ssl-images-amazon.com/images/I/51gEpO63aRL.jpg'
        },
        {
          'id': 3,
          'title': 'Titanic',
          'year': 1997,
          'prob': 0.9,
          'img': 'https://images-na.ssl-images-amazon.com/images/I/51gEpO63aRL.jpg'
        },

      ],
      fav: [], //lista użytkownika który dodał do
      user_selection: [] // to co wybrał użytkownik
    }
  },
  mounted() {
    this.get_cold_movie();
  },
  methods: {
    get_cold_movie() {
         var v = this;
         var request = new XMLHttpRequest();
          request.open('POST', 
          'https://klemenko.pl:8000/movies_cold',
           true);

           // let im = _base64ToArrayBuffer(image);
          //  console.log(im);  
           //Creates the FormData object and attach to a key name "file"
          //  var fd = new FormData();
          //  fd.append("file", image);

          request.onload = function () {
            
             // Begin accessing JSON data here
            var data = JSON.parse(this.response);

            console.log(data.list);
            v.movies = data.list;
            //  v.name = data.predicted;
            //  let pred = Math.round(data.prob*10000)/100;
            //  v.pred = pred;
            //  console.log('some data:', pred);

            }
          request.onerror = function () {
            console.warn('Some error', request.status)
          }
          // Send request
          request.send();

    },

    get_movies() {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
