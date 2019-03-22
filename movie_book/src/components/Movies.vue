<template>
  <div id="body" class="body">
    <!-- <div class="details "> -->
    <MovieDetails
      v-if="is_details"
      class="animated fadeInRight  faster"
      :movie='detail_item'
      @fav_add='fav_add(detail_item)'
      @fav_rem='fav_rem(detail_item)'
      @back='is_details = false'
    />

    <div class="header">
      <span class="left">
        <button title="Books recommendation" class="btn btn-over" @click="$router.push('books')"><i class="fas fa-book"></i></button>
        <button title="About" class="btn btn-over" @click="$router.push('about')"><i class="far fa-address-card"></i></button>
      </span>

      <h1 class="header-title">{{$data.path}} Movies recommendation</h1>
    </div>

    <div
      id="favs-header"
      class=" "
    >
      <!-- <h2
        class="title"
 
      > <i class="fas fa-star"></i> To watch ({{fav.length}}):</h2> -->

   <h2 class="title watch"    @click="fav_visible = !fav_visible"    >
     <button   class="btn btn-back"><i class="fas fa-star"></i> To watch ({{fav.length}}):
     </button>
     </h2>

      <div
        v-show="fav_visible"
        id="favs"
        class="cards  scrollbar-x animated bounceInDown"
      >
        <card
          v-for="m in fav"
          :key="m.movie_ix"
          :value="m"
          :islist="false"
          :description="m.year"
          :img="m.img"
          @click="show_details(m)"
          @fav_rem="fav_rem(m)"
        />
      </div>
    </div>

    <h2 class="title recommendation" ><button :disabled="!is_minimum" @click="recommendation_get" class="btn btn-back"><i class="fas fa-trophy"></i>  Find Recommendations 
   <span v-if="!is_minimum">(required another {{MIN_REQUIRED-rates.length}} rates)</span> :</button>
</h2>

    <div
      id="movies"
      class="cards scrollbar"
    >
<div class="dot-bricks" v-if="is_loading"></div>
    
      <div
        v-for="m in movies"
        :key="m.movie_ix"
        class="animated bounceIn"
      >
        <!-- <transition name="fade"> -->

        <card
          :value="m"
          :islist="true"
          @fav_add="fav_add(m)"
          @rate="rate"
          @click="show_details(m)"
          @not_seen="not_seen_add(m)"
        />
        <!-- </transition> -->
      </div>

    </div>

  </div>

</template>

<script>
import Vue from "vue";
import MovieDetails from "./MovieDetails.vue";

const URL = "https://klemenko.pl:8005/";
// const URL = "http://localhost:8005/";

const MIN_REQUIRED = 20;
const URL_COLD = URL + "movies_cold";
const URL_REPLACE = URL + "movies_replace"; //<- get next movie from the PCA
const URL_GET = URL + "movies_get"; //<- get movies recommendations

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function sleep(ms = 300) {
    await timeout(ms);
}

export default {
  name: "HelloWorld",
  data() {
    return {
      MIN_REQUIRED: MIN_REQUIRED, //<- minimum number of recommendation
      detail_item: "",
      is_details: false, //<- is show details full screen
      fav_visible: true,
      is_loading: false, //we loading the whole page
      movies: [], //list of current movies
      not_seen: [], //list of not selected
      fav: [],        //lista użytkownika który dodał do
      rates: [] // to co wybrał użytkownik (wysyłane do recommendation)
    };
  },
  computed: {
    is_minimum() {
      return this.rates.length >= this.MIN_REQUIRED;
    }
  },
  components: {
    MovieDetails
  },
  mounted() {
    this.get_cold_movie();
  },
  methods: {
   
    fav_add(m) {
      if(m.is_fav) return;
      if(this.fav.indexOf(m.is_fav) >= 0) {
        m.is_fav = true;
        return;
      }
      m.is_fav = true;
      this.fav.push(m);
      this._replace_movie(m);
    },
    fav_rem(m) {
      m.is_fav = false;
      this.fav.splice(this.fav.indexOf(m), 1);
    },

    show_details(m) {
      //go to the full screen, and show details about movie.
      this.detail_item = m;
      this.is_details = true;
      // console.log(this.is_details);
    },


    async _replace_movie(m) {
      m.is_loading = true;
      let v = this;

      //we need to go the movies
      var request = new XMLHttpRequest();
      request.open("POST", URL_REPLACE, true);
      request.onload = function() {
        // Begin accessing JSON data here
        // console.log(this.response);
        var data = JSON.parse(this.response)[0];
        // console.log(data);

        var index = v.movies.indexOf(m);
        if (index !== -1) {
          data.is_loading = false;
          // v.movies[index] = data;
          Vue.set(v.movies, index, data); // replace value with new one
        }
      };
      request.onerror = function() {
        console.warn("Some error", request.status);
      };
      request.send(JSON.stringify(await this._get_all_movies())); //<movies to exclude from the df
    },

    async   not_seen_add(m) { //remove movie from the list
      if(this.not_seen.indexOf(m)<0) //add to not seen if deosn't exist
      {
        this.not_seen.push(m);
      };
      await this._replace_movie(m);
    },

   async rate(m, is_fav = false) {
      var v = this;
      if(v.rates.indexOf(m)>=0) return;
      v.rates.push(m);
    },    


    async recommendation_get() {
      let v = this;
      v.movies = [];
      v.is_loading = true;

      // await sleep(3000); //just to check loading;

      // based on the rates we return list of movies
      var request = new XMLHttpRequest();
      request.open("POST", URL_GET, true);
      request.onload = function() {
        // Begin accessing JSON data here
        // console.log(this.response);
        v.is_loading = false;
        
        var data = JSON.parse(this.response);

        // console.log(data);
        for (var m of data) {
          console.log(m.movie_ix, m.title)
          m.is_loading = false;
          m.is_fav = false;
          v.movies.push(m);
        }
        // console.log(data)
      };
      request.onerror = function() {
        console.warn("Some error", request.status);
      };
      // Send request
      request.send(JSON.stringify(
        [await this._get_rates_movies(),
        await this._get_to_watch_movies()]));
    },

    get_cold_movie() {
      var v = this;
      var request = new XMLHttpRequest();
      request.open("POST", URL_COLD, true);
      request.onload = function() {
        // Begin accessing JSON data here
        // console.log(this.response);
        var data = JSON.parse(this.response);
        // console.log(data);
        for (var m of data) {
          m.is_loading = false;
          m.is_fav = false;
          v.movies.push(m);
        }
      };
      request.onerror = function() {
        console.warn("Some error", request.status);
      };
      // Send request
      request.send();
    },
    
    async _get_all_movies() { // get all movies that was show to the user.
        //get list of movies, with raitings
        //we add movies to set-up what it is was
        // function get_movies(movies, is_fav = false) {
        var data = [];
        for (var m of this.movies) {
             data.push(m.movie_ix);
        }        
        for (var m of this.rates) {
         if(data.indexOf(m<0)) {
             data.push(m.movie_ix);
          }
        }
        for (var m of this.not_seen) {
          if(data.indexOf(m<0)) {
             data.push(m.movie_ix);
          }
        }
        for (var m of this.fav) {
          if(data.indexOf(m<0)) {
             data.push(m.movie_ix);
          }
        }
        console.log(data);
        return data;
    },
    async _get_rates_movies() { // get all movies
        //get list of movies, with raitings
        //we add movies to set-up what it is was
        // function get_movies(movies, is_fav = false) {
        var data = [];
        for (var m of this.rates) {
          data.push([m.movie_ix, m.rate]);
        }
        return data;
    },    

    // get movies that are to watch
    async _get_to_watch_movies() {
        var data = [];
        for (var m of this.fav) {
          data.push(m.movie_ix);
        }
        return data;
    }

  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style  lang="scss">
@import "../css/main.scss";

$row-height: 300px;
$header-height: 450px;

$color-silver: #dfe4ea;
$color-gray: #57606f;
$color-gray-2: #2f3542;
$color-black: #57606f;
$scale: 0.96;
$card-height: 180px;

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

.body {
  // margin-left: auto;
  // margin-right: auto;

  width: 100%;
  height: 100%;

  // margin: 20px;

  color: white;

  //  display: grid;
  width: 100%;
  height: 100%;

  // grid-template-columns: 1fr;
  // grid-template-rows: auto 1fr;
  padding: 20px;

  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: auto auto auto 1fr;
  max-height: 100%;


  .content {
    // margin: 20px;
    overflow: hidden;
    width: 100%;
    height: 100%;
    max-height: 100%;
  }

  // display: flex;
  // flex-direction: column;
  // flex-wrap: nowrap;
  @media (max-width: 320px) {
    /* CSS that should be displayed if width is equal to or less than 800px goes here */
    h1 {
      font-size: 1.2rem;
    }

    h2 {
      font-size: 1rem;
    }
  }

  @media (max-width: 800px) {
    /* CSS that should be displayed if width is equal to or less than 800px goes here */
    h1 {
      font-size: 1.7rem;
    }

    h2 {
      font-size: 1.2rem;
    }
  }

  @media (min-width: 800px) {
    /* CSS that should be displayed if width is equal to or less than 800px goes here */
    //  font-size: 24px;
  }

  .header {
    width: 100%;

    display: flex;

    .left {
      display: inline;
      margin-right: 2rem;
    }

      h2 {
        display: inline;
      }

      .header-title {
        color: rgba($color-white,0.9);
      }

  }

  .title {
    cursor: pointer;
    margin-top: 5px;
    // margin-right: auto;
    display: block;
    text-align: left;
    margin-left: 0.5rem;

    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 0;

      /// Remove blue highligh on click
  -webkit-tap-highlight-color: transparent;
  -moz-tap-highlight-color: transparent;
  -o-tap-highlight-color: transparent;
  tap-highlight-color: transparent;
  outline: none;

    &.watch * {
         box-shadow: 0px 0px 2px $color-star;
        background-color: $color-star;
        color: $color-gray;

        
    }
    

    &.recommendation {
      margin-top: 0.5rem;

      :disabled {
        transition: none !important;
        
          background: $color-gray;

        * {
          background: $color-gray;
        }
      }
      * {
        background: $color-blue;
        color: white;
      }
    }
  }
}

#favs-header {
  overflow: auto;
  margin-right: 0;
  // height: $row-height;
  // margin-left: 2rem;

  overflow-y: hidden;
  #favs {
    display: flex;
    flex-wrap: nowrap;
    overflow: auto;
    overflow-y: hidden;
    align-content: flex-start;
    justify-content: flex-start;

    height: auto;
    width: 100%;
  }
}

#movies {
  width: 100%;
  // height: -moz-calc(100vh - (350px));
  // height: -webkit-calc(100vh - (350px));
  // height: calc(100vh - (350px));
  overflow: auto;

  // max-height:100%;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
