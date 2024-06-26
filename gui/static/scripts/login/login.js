// GO HERE => https://github.com/mrdoob/three.js/blob/master/examples/canvas_particles_waves.html

const SEPARATION = 100,AMOUNTX = 12,AMOUNTY = 12;
// let container, stats;
let container;
let camera, scene, renderer;
let particles,particle,count = 0;
let mouseX = 0,mouseY = 0;
let windowHalfX = window.innerWidth / 2;
let windowHalfY = window.innerHeight / 2;

function init() {
  container = document.createElement('div');
  document.body.appendChild(container);
  camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 10000);
  camera.position.z = 500; // Good var to change
  scene = new THREE.Scene();
  particles = new Array();
  var PI2 = Math.PI * 2;
  var geometry = new THREE.Geometry();
  var material = new THREE.SpriteCanvasMaterial({
    color: 0x000000,
    program: function (context) {
      context.beginPath();
      context.arc(0, 0, 0.4, 0, PI2, true);
      context.fill();
    } });



  var i = 0;
  for (var ix = 0; ix < AMOUNTX; ix++) {
    for (var iy = 0; iy < AMOUNTY; iy++) {
      particle = particles[i++] = new THREE.Sprite(material);
      particle.position.x = ix * SEPARATION - AMOUNTX * SEPARATION / 2;
      particle.position.z = iy * SEPARATION - AMOUNTY * SEPARATION / 2;
      scene.add(particle);

      if (i > 0) {
        geometry.vertices.push(particle.position);
      }
    }
  }

  // var line = new THREE.Line(geometry, new THREE.LineBasicMaterial({
  //   color: 0xffffff,
  //   opacity: 0.5,
  //   linewidth: 4
  // }));
  // scene.add( line );

  renderer = new THREE.CanvasRenderer();
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  container.appendChild(renderer.domElement);
  // stats = new Stats();
  // container.appendChild(stats.dom);
  document.addEventListener('mousemove', onDocumentMouseMove, false);
  document.addEventListener('touchstart', onDocumentTouchStart, false);
  document.addEventListener('touchmove', onDocumentTouchMove, false);
  //
  window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
  windowHalfX = window.innerWidth / 2;
  windowHalfY = window.innerHeight / 2;
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function onDocumentMouseMove(event) {
  mouseX = event.clientX - windowHalfX;
  mouseY = event.clientY - windowHalfY;
}

function onDocumentTouchStart(event) {
  if (event.touches.length === 1) {
    event.preventDefault();
    mouseX = event.touches[0].pageX - windowHalfX;
    mouseY = event.touches[0].pageY - windowHalfY;
  }
}

function onDocumentTouchMove(event) {
  if (event.touches.length === 1) {
    event.preventDefault();
    mouseX = event.touches[0].pageX - windowHalfX;
    mouseY = event.touches[0].pageY - windowHalfY;
  }
}

function animate() {
  requestAnimationFrame(animate);
  render();
  // stats.update();
}

function render() {
  renderer.setClearColor(0x755ee5, 1);
  camera.position.x += (mouseX - camera.position.x) * .05;
  camera.position.y += (-mouseY - camera.position.y) * .05;
  camera.lookAt(scene.position);
  var i = 0;
  for (var ix = 0; ix < AMOUNTX; ix++) {
    for (var iy = 0; iy < AMOUNTY; iy++) {
      particle = particles[i++];
      particle.position.y = Math.sin((ix + count) * 0.3) * 50 + Math.sin((iy + count) * 0.5) * 50;
      particle.scale.x = particle.scale.y = (Math.sin((ix + count) * 0.3) + 1) * 4 + (Math.sin((iy + count) * 0.5) + 1) * 5;
    }
  }
  renderer.render(scene, camera);
  count += 0.06;
}

init();
animate();