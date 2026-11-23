import { Component } from '@angular/core';
import { KolikkopeliView } from '../components/kolikkopeli-view/kolikkopeli-view';

@Component({
  imports: [KolikkopeliView],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {}

