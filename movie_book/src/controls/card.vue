<style lang="scss">
@import "../css/main.scss";

$color-silver: #dfe4ea;
$color-gray: #57606f;
$color-gray-2: #2f3542;
$color-black: #57606f;
$scale: 0.96;
$card-height: 180px;

h2 {
  margin-bottom: 1rem;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  // justify-content: space-between;
  // border: 10px solid red;
  padding: 0px;
  margin: 0px;

  // margin-top: 0.5rem;
  padding-top: 1.5rem;

  overflow: visible;

  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;

  align-content: flex-start;

  // &::after {
  //   content: '';
  //   flex: auto;
  //           // margin: 0;
  //   // margin-right: 0
  //   // margin-left: -50px;
  //   // width: 240px;
  // }

  a,
  a:link,
  a:hover,
  a:active,
  p:hover,
  a:-webkit-any-link,
  .noDecoration,
  a:link,
  a:visited {
    text-decoration: none;
    text-decoration: none !important;
    box-shadow: none;
  }
  > p {
    margin: 0;
    margin-right: 0;
    margin-left: 0;
    display: block;
  }

  .item {
    margin: 0;
    margin-right: 0;
    margin-left: 0;
    position: relative;

    // width: 180px;
    // height: 280px

    // &.isLoading {
    //   background: red;
    // }

    .user-popover {
        position: absolute !important;
        width: 180px;
        padding: 5px;
        
//  width: 0;
//       height: 0;
      // bottom: -50px;
      // left: 22px;
top: -15px;
      left: 25px;

      display: inline-block;
      // border-top: 6px solid lighten(#1BA39C, 80%);
      // border-right: 6px solid transparent;
      // border-bottom: 6px solid transparent;
      // border-left: 6px solid transparent;      
      // content: "";
      // opacity: 1.0;
      // transition: .3s;
      font-size: 12px;

        // color: black;
        border: 1px solid #42b983;
background: #57606f;
        border-radius: 5px;
        // background: white;
        // padding: 10px 20px;
        // box-shadow: 0 6px 6px rgba(16, 16, 16, 0.04), 0 6px 6px rgba(0, 0, 0, 0.05);
        z-index: 93999;

    
    }
  }

  .card {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    border: 0;
    margin-left: 10px;
    margin-right: 10px;
    width: 180px;
    height: 240px;

    /// Remove blue highligh on click
    -webkit-tap-highlight-color: transparent;
    -moz-tap-highlight-color: transparent;
    -o-tap-highlight-color: transparent;
    tap-highlight-color: transparent;

    // margin-right: 15px;

    // margin-right: 5px;
    border: 1px $color-silver;
    margin-bottom: 10px;
    margin-top: 5px;

    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    cursor: pointer;

    .card-loading {
      background: transparent;
      color: black;

      margin-left: auto;
      margin-right: auto;
      display: block;
      padding-top: 55px;

      .dot-bricks {
        // left: 20px;
        margin-top: 0 !important;
        // padding-top: 45px !important;
      }
    }

    .card-show {
      background: white;
      // color: $color-text !important;
      height: 240px;

      h4 {
        color: $color-text;
      }
    }

    &:hover {
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
      transform: translateY(-5px); // top: -10px;
    }
    &:active {
      transform: scaleX($scale) scaleY($scale);
    }

    .badges {
      position: absolute;
      margin-left: 5px;
      margin-top: 5px;
      display: flex;
    }

    .lang {
      position: absolute;
      right: 10px;
      top: 5px;
      opacity: 0.7;
    }

    img.background {
      width: 180px;
      height: $card-height;
      background-size: cover;
      object-fit: cover;
      object-position: 0 0;
      border-bottom: 1px solid $color-silver;
    }

    .image-top {
      position: relative;

      .rating {
        position: absolute;
        left: 12px;
        top: 10px;
        border: 1px solid $color-star;
      }

      .minus {
        box-shadow: 0px 0px 2px $color-red;
        background-color: $color-red;
        // opacity: 0;

        right: 2px;
        bottom: -10px;
        position: absolute;

        &:hover .tooltip {
          display: block;
        }

        .tooltip {
          position: absolute;
          display: none;

          width: 100px;
          // height: 180px;
          right: 20px;
          bottom: 45px;
          padding: 0.3rem;
          border-radius: 12px;

          background-color: rgba($color-red, 0.8);
          z-index: 1016;
        }
      }
      .not-favorite {
        box-shadow: 0px 0px 2px $color-pink;
        background-color: $color-pink;
        // margin-top: -70px;
        // margin-right: -30px;
        right: 32px;
        .fas {
          margin-top: 2px;
        }
        bottom: -10px;
        position: absolute;
        z-index: 102;

        &:hover .tooltip {
          display: block;
        }

        .tooltip {
          position: absolute;
          display: none;

          width: 70px;
          // height: 180px;
          right: 20px;
          bottom: 45px;
          padding: 0.3rem;
          border-radius: 12px;

          background-color: rgba($color-pink, 0.8);
          z-index: 1016;
        }
      }

      .favorite {
        box-shadow: 0px 0px 2px #d8ab00;
        background-color: #f1c40f;
        // margin-top: -70px;
        // margin-right: -30px;
        right: 0px;
        bottom: -10px;
        position: absolute;

        &:hover .tooltip {
          display: block;
        }

        .tooltip {
          position: absolute;
          display: none;

          width: 100px;
          // height: 180px;
          right: 20px;
          bottom: 45px;
          padding: 0.3rem;
          border-radius: 12px;

          background-color: rgba(#f1c40f, 0.8);
          z-index: 1016;
        }
      }
    }

    .content {
      margin-top: 0;
      padding: 0px 16px 5px 16px;
      .badge {
        margin-left: 5px;
      }

      &:hover {
        text-decoration: none !important;
      }
      // height: 120px;

      .title {
        margin: 0;
        display: flex;
        margin-top: 5px;
        justify-content: space-between;
        font-size: 0.8rem;

        /* 100 = viewport width, as 1vw = 1/100th of that
       So if the container is 50% of viewport (as here)
       then factor that into how you want it to size.
       Let's say you like 5vw if it were the whole width,
       then for this container, size it at 2.5vw (5 * .5 [i.e. 50%])
        */
        // font-size: 1.3vw;
        @media (min-width: 800px) {
          /* CSS that should be displayed if width is equal to or less than 800px goes here */
          font-size: 0.8rem;
        }

        text-overflow: ellipsis;
        white-space: nowrap;
        width: 100%;
        max-width: 150px;

        h4 {
          display: inline;
          margin-right: auto;
          margin: 0;
          padding: 0;
          max-width: 150px;

          text-overflow: ellipsis;
          white-space: nowrap;
          max-width: 150px;

          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .year {
          display: inline;

          color: #57606ffb;
          text-align: right;
          font-size: 0.8rem;
          font-weight: 600;
        }
      }

      p.text {
        text-align: justify;
        color: $color-black;
        text-decoration: none;
        font-size: 0.7rem;
        margin: 0;
        padding: 0;

        &:hover {
          text-decoration: none;
        }
      }
    }
  }
}
</style>

<template>
  <div class="item"

  v-on:mouseover="hover" v-on:mouseout="hoverOut"
  >

      <div class="user-popover" 
     v-if="showPopup"
      transition="fade" 
      v-on:mouseover="hoverInfo" 
      v-on:mouseout="hoverOutInfo">
      <span class="rating-small">{{value.rating}}</span>
{{value.plot.substring(0,100)}}...
      </div>

    <a
      :href="link"
      class="noDecoration"
    >

      <div
        class="card"
        @click="$emit('click')"
      >

      <!-- where there is loading -->
        <div
          v-if="value.isLoading"
          class="card-loading "
        >
          <div class="dot-bricks"></div>
        </div>

        <div
          class="card-show"
          v-else
        >
          <div class="image-top">
            <img
              class="background"
              :src="value.cover"
              alt="Card image cap"
            >

            <!-- <span class="rating">{{value.rating}} </span>  -->


            <button
              class="btn-round minus"
              v-if="!islist"
              @click.stop="$emit('fav_rem')"
            >
              <i class="fas fa-minus"></i>
              <div class="tooltip">
                I don't wanna watch it
              </div>
            </button>

            <button
              class="btn-round not-favorite"
              v-if="islist"
              @click.stop="$emit('not_seen')"
            >
              <i class="fas fa-thumbs-down"></i>
              <div class="tooltip">
                <i class="fas fa-thumbs-down"></i>
                Not seen
              </div>
            </button>

            <button
              class="btn-round  favorite"
              v-if="islist"
              @click.stop="$emit('fav_add')"
            >
              <i class="fas fa-star"></i>

              <div class="tooltip">
                <i class="fas fa-star"></i>
                Add to watch
              </div>
            </button>

          </div>

          <div class="content">
            <star-rating
              :rating="value.rate"
              @rating-selected="rate"
              :show-rating="false"
              :increment="0.5"
              :star-size="20"
            />

            <div class="title">
              <h4>{{value.title}}</h4>
              <span class="year">{{value.year}}</span>
            </div>
            <!-- <p class="text">{{description}}</p> -->
          </div>

        </div>

      </div>

    </a>

  </div>
</template>

<script>
function isMobileDevice() {
  return (
    typeof window.orientation !== "undefined" ||
    navigator.userAgent.indexOf("IEMobile") !== -1
  );
}

export default {
  data() {
    return {
      /** POPUP DATA */
			showPopup: false,
			timer: '',
			isInInfo: false
    }

  },
  props: [
    "value",
    // "title",
    "islist",
    // "year",
    // "badge",
    // "description",
    // "lang",
    // "img",
    "link"
  ],
  computed: {
    badges() {
      if (this.badge == null || this.badge == "") return [];
      return this.badge.split(",");
    },

    isMobile() {
      return (
        typeof window.orientation !== "undefined" ||
        navigator.userAgent.indexOf("IEMobile") !== -1
      );
    }
  },
  methods: {
    rate(val) {
      // console.log(val);
      this.value.rate = val;
      this.$emit("rate", this.value);
    },

    /** POPUP METHODS */
    hover: function()
    {
      let vm = this;
      this.timer = setTimeout(function() {
        vm.showPopover();
      }, 300);
    },

    hoverOut: function()
    {
      let vm = this;
      clearTimeout(vm.timer);
      this.timer = setTimeout(function() {
        if(!vm.isInInfo)
        {
          vm.closePopover();
        }
      }, 200);
    },

    hoverInfo: function()
    {
      this.isInInfo = true;
    },
    
    hoverOutInfo: function()
    {
      this.isInInfo = false;
      this.hoverOut();
    },

    showPopover: function()
    {
      this.showPopup = true;
    },

    closePopover: function()
    {
      this.showPopup = false;
    }
  }
};
</script>
