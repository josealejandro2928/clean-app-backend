Vue.component('app-about-us', {
  template: `
      <section class="about">
        <div class="card" style="width: 60rem; max-width: 100%; position: relative;margin-bottom:1rem">
          <p class="text">
            <img src="static/images/jose.jpg"/>
              Jose Alejandro Concepcion Alvarez is currently enrolled on the PhD of Computer Science, GSSI. Previously he was a Training Professor at the Microelectronic Department, the Technological University of Havana “José Antonio Echeverría”. He obtained a MSc in Automation Engineering 
              from the Technological University of Havana “José Antonio Echeverría”. He has experience in analyzing and designing algorithms 
              and software engineering, in the last 2 years he was working as a software developer for Cuban and International companies. 
              His current research interests are Software Architectures for Distributed Systems and Cloud Computing, Machine Learning, 
              Development software for code generation, Robotics, and Cyber-Physical Systems.
          </p>
          <ul>
            <li>
              <a target="_blank" href="https://github.com/josealejandro2928">github</a>
              <a target="_blank" href="https://www.gssi.it/people/students/students-computer-science/item/15643-concepcion-alvarez-jose-aleandro">gssi</a>
              <a target="_blank" href="https://www.linkedin.com/in/jalejandroc/">linkedin</a>
            </li>
          </ul>
        </div>
        <div class="card" style="width: 60rem; max-width: 100%; position: relative;margin-bottom:1rem">
          <p class="text">
            <img src="static/images/tony.jpg"/>
            Juan Antonio Pinera Garcia is currently enrolled on the PhD of Computer Science, GSSI. Previously he was a Training Professor at the Computer Engineering Department, 
            Technological University of Havana (Cuba) and a Research Fellow at the “Group of Robotics and Mechatronics”, Technological University of 
            Havana(Cuba), where he co-led multiple projects to apply robotics to help solve everyday problems in multiple escenarios. He was awarded 
            multple prizes in international robotics conventions, such as “Robotic People Fest”, Colombia. In addition, he participated in a r
            esearch group “Fault Diagnosis”, where multiple machine learning methods were applied to analyze the sensorial data from several factories 
            from Havana and predict possible failures in the near future.
          </p>
          <ul>
            <li>
              <a target="_blank" href="https://github.com/tonypg39">github</a>
              <a target="_blank" href="https://www.gssi.it/people/students/students-computer-science/item/15647-pinera-garcia-juan-antonio">gssi</a>
            </li>
          </ul>
        </div>
      </section>
    
    `,
});

// eslint-disable-next-line no-unused-vars
let app = new Vue({
  el: '#app',
  data: {
    title: 'About Us',
    subTitle: '',
  }

})