var close = document.querySelector(".close");
var open = document.querySelector(".open");
var popUp = document.querySelector(".popUp");
var popUpContainer = document.querySelector(".popUp-container");

var closeRegister = document.querySelector(".close-register");
var openRegister = document.querySelector(".registerOpen");
var popUpContainerRegister = document.querySelector(".popUp-containerRegister");
var popUpRegister = document.querySelector(".popUp-register");

// lateral
var lateralInfo = document.querySelector(".lateralInfo");
var activeLateral = document.querySelector(".hambur");
var desactivarLateral = document.querySelector(".desactivar");

// calculadora importe
let inputNombre = document.querySelector(".inputNombre");
let inputPrecio = document.querySelector(".inputPrecio");
let boton = document.querySelector("#boton");
let contResultados = document.querySelector("#resultados");
let total = document.querySelector("#total");
let aporte = document.querySelector("#aporte");

// Doalr hoy
let bodyDivisa = document.querySelector("#bodyDivisa");
let inputDolar = document.querySelector("#inputDolar");
let inputPeso = document.querySelector("#inputPeso");

open.addEventListener("click", function (e) {
  e.preventDefault();
  popUpContainer.style.opacity = "1";
  popUpContainer.style.visibility = "visible";
  popUp.classList.toggle("popUp-close");
});

openRegister.addEventListener("click", function (e) {
  e.preventDefault();
  popUpContainerRegister.style.opacity = "1";
  popUpContainerRegister.style.visibility = "visible";
  popUpRegister.classList.toggle("popUp-closeRegister");
});

close.addEventListener("click", function (e) {
  e.preventDefault();
  popUp.classList.toggle("popUp-close");
  setTimeout(() => {
    popUpContainer.style.opacity = "0";
    popUpContainer.style.visibility = "hidden";
  }, 320);
});

closeRegister.addEventListener("click", function (e) {
  e.preventDefault();
  popUpRegister.classList.toggle("popUp-closeRegister");
  setTimeout(() => {
    popUpContainerRegister.style.opacity = "0";
    popUpContainerRegister.style.visibility = "hidden";
  }, 320);
});

window.addEventListener("click", function (e) {
  if (e.target == popUpContainer) {
    popUp.classList.toggle("popUp-close");
    setTimeout(() => {
      popUpContainer.style.opacity = "0";
      popUpContainer.style.visibility = "hidden";
    }, 320);
  }
});

activeLateral.addEventListener("click", function () {
  lateralInfo.classList.toggle("activo");
  activeLateral.style.opacity = "0";
  activeLateral.style.visibility = "hidden";
});

desactivarLateral.addEventListener("click", function () {
  lateralInfo.classList.toggle("activo");
  activeLateral.style.opacity = "1";
  activeLateral.style.visibility = "visible";
});

// Calculadora
const usuarios = [];

boton?.addEventListener("click", (e) => {
  e.preventDefault();
  contResultados.innerHTML = "";

  usuarios.push({
    nombre: inputNombre.value,
    precio: Number(inputPrecio.value),
  });

  let sumaTotal = 0;
  for (let i = 0; i < usuarios.length; i++) {
    contResultados.innerHTML += `<li><span class='span-calc'>${usuarios[i].nombre}</span>: $${usuarios[i].precio}</li>`;
    sumaTotal += usuarios[i].precio;
  }
  total.innerHTML = `<span class='span-calc'>Total</span>: $${sumaTotal}`;

  aporte.innerHTML = `<span class='span-calc'>Cada uno debe aportar</span>: $${
    sumaTotal / usuarios.length
  }`;

  inputNombre.value = "";
  inputPrecio.value = "";
});

// Dolar hoy

window.onload = function () {
  mostrar();
};

const data = async () => {
  const response = await fetch(
    "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
  );

  const data = await response.json();

  return data;
};

const mostrar = async () => {
  const dataDolar = await data();
  for (const dolar of dataDolar) {
    let divisa = document.createElement("td");
    let compra = document.createElement("td");
    let venta = document.createElement("td");
    let tr = document.createElement("tr");

    divisa.innerHTML = dolar.casa.nombre;
    compra.innerHTML = dolar.casa.compra;
    venta.innerHTML = dolar.casa.venta;

    tr.appendChild(divisa);
    tr.appendChild(compra);
    tr.appendChild(venta);

    compra.classList.add("table-derecha");
    venta.classList.add("table-derecha");

    bodyDivisa.appendChild(tr);
  }
};

inputPeso.addEventListener("change", async () => {
  const dataDolar = await data();
  inputDolar.value =
    Number(inputPeso.value) /
    (Number(dataDolar[0].casa.venta.replace(",", ".")) * 1.65);
});

inputDolar.addEventListener("change", async () => {
  const dataDolar = await data();
  inputPeso.value =
    Number(inputDolar.value) *
    (Number(dataDolar[0].casa.venta.replace(",", ".")) * 1.65);
});
