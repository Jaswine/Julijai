//TODO: home page
const galery_massive = ['https://images.pexels.com/photos/1707820/pexels-photo-1707820.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/315191/pexels-photo-315191.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/1089194/pexels-photo-1089194.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/3352384/pexels-photo-3352384.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' , 'https://images.pexels.com/photos/8005438/pexels-photo-8005438.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://images.pexels.com/photos/351961/pexels-photo-351961.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/2393789/pexels-photo-2393789.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/735273/pexels-photo-735273.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/4049876/pexels-photo-4049876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/5417622/pexels-photo-5417622.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/11632932/pexels-photo-11632932.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/2826131/pexels-photo-2826131.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/3201580/pexels-photo-3201580.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/2067569/pexels-photo-2067569.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1','https://images.pexels.com/photos/3747315/pexels-photo-3747315.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1','https://images.pexels.com/photos/970080/pexels-photo-970080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/1019771/pexels-photo-1019771.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/4394970/pexels-photo-4394970.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/3491680/pexels-photo-3491680.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'https://images.pexels.com/photos/2197924/pexels-photo-2197924.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1']

let intro__phone = document.querySelector('.intro__phone');

for (let i=0; i<=20; i+=1 ) {
    let rand = Math.floor(Math.random()*galery_massive.length);
    let result = galery_massive[rand]
    //console.log(result);
    let a = `<img src='${result}'>`
    intro__phone.append(a);//ok we add img in <div class="intro__phone"></div> but it's doesn't work
}

let intro__phone__childs = intro__phone.childNodes;
let for__intro__phone = ''

for (let i=0; i<intro__phone__childs.length;i++) {
    let intro__phone__child = intro__phone__childs[i];
    for__intro__phone += intro__phone__child.wholeText;
}

console.log(for__intro__phone)
intro__phone.innerHTML = for__intro__phone;
