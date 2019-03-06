<template>
  <div class="hello">
  
<div id="favs-header">
  
   <h2 class="title">   <i class="fas fa-star"></i> To watch ({{fav.length}}):</h2>

    <div id="favs" class="cards  scrollbar-x">
          <card v-for="m in fav" :key="m.id"
          :title="m.title"

                  :year="m.year"
          :islist="false"
          :description="m.year"
          :img="m.img"

          @fav_rem="fav_rem(m)"
          />
    </div>
</div>

  <h2 class="title">Recommended:</h2>
    <div id="movies" class="cards scrollbar">
           <card v-for="m in movies" :key="m.id"
           :islist="true"
        :title="m.title"
        :year="m.year"
        :img="m.img"

        @fav_add="fav_add(m)"
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
    fav_rem(m) {
     this.fav.splice( this.fav.indexOf(m), 1 );
    },
    fav_add(m) {
      this.fav.push(m)
      // console.log(m,this.fav)
    },
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

            // for(i=0;i<10;i++) {
             
            // }
            v.movies = data.list;

            // v.movies.push(...data.list); //add new array
            // v.movies.push(...data.list); //add new array
            // v.movies.push(...data.list); //add new array
            // v.movies.push(...data.list); //add new array

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

.hello {
  // margin-left: auto;
  // margin-right: auto;

  width: 100%;
  height: 100%;

  // display: flex;
  // flex-direction: column;
  // flex-wrap: nowrap;


  .title {
    // margin-right: auto;
    display: block;
    text-align: left;

    color: rgba(255,255,255,0.9);
    margin-bottom: 0;
  }

  display: grid;
  grid-template-columns:   1fr;
  grid-template-rows: 270px 25px 100%;  
  max-height:100%;
}

#favs-header {
  overflow: auto;
  margin-right: 0;
  height: 270px;
  // margin-left: 2rem;
    #favs {
      display: flex;
      flex-wrap: nowrap;
      overflow: auto;
      align-content: flex-start;
      justify-content: flex-start;

      height: auto;
      width: 100%;
    }
}


  #movies {
    width: 100%;
    height: -moz-calc(100vh - (380px));
    height: -webkit-calc(100vh - (380px));
    height: calc(100vh - (380px));
    overflow: auto;

      // max-height:100%;
  }



</style>
