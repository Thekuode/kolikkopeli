import { Component, inject, signal } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

export interface RollResult {
  user: string;
  bet: number;
  reels: string[];
  payout: number;
  net: number;
  win: boolean;
  balance: number;
}

@Component({
  selector: 'app-kolikkopeli-view',
  templateUrl: './kolikkopeli-view.html',
  styleUrl: './kolikkopeli-view.css',
})
export class KolikkopeliView {
  private readonly http = inject(HttpClient);
  private readonly apiUrl = 'http://localhost:8000/api/roll';

  readonly result = signal<RollResult | null>(null);
  readonly error = signal<string | null>(null);
  readonly loading = signal(false);

  async spin(): Promise<void> {
    this.loading.set(true);
    this.error.set(null);

    try {
      const data = await firstValueFrom(this.http.get<RollResult>(this.apiUrl));
      this.result.set(data);
    } catch (err) {
      const httpErr = err as HttpErrorResponse;
      const detail =
        typeof httpErr.error?.detail === 'string'
          ? httpErr.error.detail
          : 'Pyöräytys epäonnistui';
      this.error.set(detail);
    } finally {
      this.loading.set(false);
    }
  }
}
