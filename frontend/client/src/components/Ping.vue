<template>
    <div>
        <div>
            <img alt="Vue logo" src="../assets/logo.png">
        </div>
        <div>
            <p>{{ msg }}</p>
        </div>
        <div>
            <form>
                <div>
                    <label>Nombre </label>
                    <input type="text">
                </div>
                <div>
                    <label>Email </label>
                    <input type="email">
                </div>
                <div>
                    <label>Edad </label>
                    <select name="" id="">
                        <option value="">18-25 years</option>
                        <option value="">26-33 years</option>
                        <option value="">34-40 years</option>
                    </select>
                </div>
                <div>
                    <label for="">Tiempo promedio al dia en Tiktok </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label for="">Tiempo promedio al dia en WhatsApp </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label for="">Tiempo promedio al dia en Twitter </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label for="">Tiempo promedio al dia en Instagram </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label for="">Tiempo promedio al dia en Facebook </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                <div>
                    <button>Cargar</button>
                </div>
                </div>
            </form>
        </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

