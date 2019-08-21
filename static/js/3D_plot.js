// Download 3D files

function saveToZip (filename, urls) {
        const zip = new JSZip()
        const folder = zip.folder('files')
        urls.forEach((url)=> {
            const blobPromise = fetch(url).then(r => {
                if (r.status === 200) return r.blob()
                return Promise.reject(new Error(r.statusText))
            })
            const name = url.substring(url.lastIndexOf('/'))
            folder.file(name, blobPromise)
        })

        zip.generateAsync({type:"blob"})
            .then(blob => saveAs(blob, filename))
            .catch(e => console.log(e));
    }
    
function create_zip() {
        
        var x = document.getElementById("tip_3D");
          if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
        
        var URLS = new Array()
    
        for(let i = 0; i < images_numbers.length; i ++){
            URLS.push(path_output + "/" + images_numbers[i] + "_texture.png") // path_statue_texture
            URLS.push(path_output + "/" + images_numbers[i] + ".mtl") // path_statue_mtl
            URLS.push(path_output + "/" + images_numbers[i] + ".obj") // path_statue_obj
        }

    saveToZip('statues-3D.zip',URLS)
}


// 3D plot

for(let i = 0; i < images_numbers.length; i ++){
    
    var path_statue_texture = path_output + "/" + images_numbers[i] + "_texture.png";
    var path_statue_obj = path_output + "/" + images_numbers[i] + ".obj";
    //var path_statue_landmark = path_output + "/" + images_numbers[i] + ".txt";
    var path_statue_landmark = path_output + "/" + images_numbers[i] + ".txt";

	var container;

	var camera, scene, renderer;

	var mouseX = 0, mouseY = 0;
	var widthDiv = document.getElementById("container-3D").offsetWidth;
	var windowHalfX = widthDiv / 4;
	var windowHalfY = window.innerHeight / 2;
	var object;

	init();
	animate();


	function init() {

		container = document.createElement( 'div' );
		document.getElementById("container-3D").appendChild( container );

		camera = new THREE.PerspectiveCamera( 45, widthDiv / window.innerHeight, 1, 200000 );
		camera.position.z = 2000;

		// scene

		scene = new THREE.Scene();

		var ambientLight = new THREE.AmbientLight( 0xcccccc, 0.4 );
		scene.add( ambientLight );

		var pointLight = new THREE.PointLight( 0xffffff, 0.8 );
		camera.add( pointLight );
		scene.add( camera );


		// manager

		function loadModel() {

			object.traverse( function ( child ) {

				if ( child.isMesh ) {
                    child.material.map = texture;
                    child.geometry.center();
                }

			} );

			scene.add( object );

		}

		var manager = new THREE.LoadingManager( loadModel );

		manager.onProgress = function ( item, loaded, total ) {
			console.log( item, loaded, total );
		};

		// texture

		var textureLoader = new THREE.TextureLoader( manager );
                
		var texture = textureLoader.load( path_statue_texture );


		// model

		function onProgress( xhr ) {

			if ( xhr.lengthComputable ) {
				var percentComplete = xhr.loaded / xhr.total * 100;
				console.log( 'model ' + Math.round( percentComplete, 2 ) + '% downloaded' );
			}
		}

		function onError() {}

		var loader = new THREE.OBJLoader( manager );

		loader.load( path_statue_obj, function ( obj ) {
			object = obj;
			camera.position = object.position;
		}, onProgress, onError );


		// Landmarks

//		var land_mark_group = new THREE.Group();
//
//        $.get(path_statue_landmark,{},function(content){
//               let lines=content.split('\n');
//
//               for(var idx in lines){
//                    let line = lines[idx]
//                    let pos = line.split(" ")
//
//                    let geometry = new THREE.SphereGeometry( 2, 32, 32 );
//                    geometry.center();
//                    let material = new THREE.MeshBasicMaterial( {color: 0xffff00} );
//                    let mesh = new THREE.Points(geometry, material)
//                    mesh.position.set(parseFloat(pos[0]), parseFloat(pos[1]), parseFloat(pos[2]))
//                    land_mark_group.add(mesh)
//               }
//
//        });
//
//        scene.add(land_mark_group)
//
//        console.log(scene['children'])

		//

		renderer = new THREE.WebGLRenderer();
		renderer.setPixelRatio( window.devicePixelRatio );
		renderer.setSize( widthDiv, window.innerHeight );
		container.appendChild( renderer.domElement );
        
		var controls = new THREE.OrbitControls( camera, renderer.domElement );

		//
		window.addEventListener( 'resize', onWindowResize, false );
	}

	function onWindowResize() {
		windowHalfX = widthDiv / 2;
		windowHalfY = window.innerHeight / 2;
        
		camera.aspect = widthDiv / window.innerHeight;
		camera.updateProjectionMatrix();
        
		renderer.setSize( widthDiv, window.innerHeight );
	}

			//

	function animate() {

		requestAnimationFrame( animate );
		render();
	}

	function render() {
		camera.lookAt( scene.position );
		renderer.render( scene, camera );
	}
    
}