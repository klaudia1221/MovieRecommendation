<style lang="scss">
@import url('../css/main.scss');

$color-silver: #dfe4ea;
$color-gray: #57606f;
$color-gray-2: #2f3542;
$color-black: #57606f;
$scale: 0.96;

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

  margin-top: 1rem;

  &::after {
    content: '';
    flex: auto;
  }



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
  }

  .card {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    border: 0;
    margin-left: 10px;
    margin-right: 10px;
    width: 220px;

    // margin-right: 15px;
    // height: 250px;
    // margin-right: 5px;
    border: 1px $color-silver;
    margin-bottom: 1rem;

    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    cursor: pointer;

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
      width: 220px;
      height: 150px;
      background-size: cover;
      object-fit: cover;
      border-bottom: 1px solid $color-silver;
    }

    .content {
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
        justify-content: space-between;

        h4 {
          display: inline;
          margin-right: auto;
          margin: 0;
          padding: 0;
        }

        .date {
          display: inline;

          color: #57606f75;
          text-align: right;
          font-size: 0.8rem;
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
  <div class="item">
    <a :href="link" class="noDecoration">
      <div class="card">
        <!-- <div class="badges">

          <badge v-for="b in badges">{{b}}</badge>
        </div> -->

        <!-- <div class="lang">
          <img :src="lang=='pl' ? $withBase('/pl.png') :  $withBase('/en.png') " width="32px" :alt="lang">
        </div> -->

        <img class="background" :src="img" alt="Card image cap">

        <div class="content">
          <div class="title">
            <h4>{{title}}</h4>
            <!-- <span class="date">{{date}}</span> -->
          </div>

          <p class="text">{{description}}</p>
        </div>
      </div>
    </a>

  </div>
</template>

<script>
export default {
  props: ['title', 'date', 'badge', 'description', 'lang', 'img', 'link'],
  computed: {
    badges() {
      if (this.badge == null || this.badge == '') return []
      return this.badge.split(',')
    }
  }
}
</script>
