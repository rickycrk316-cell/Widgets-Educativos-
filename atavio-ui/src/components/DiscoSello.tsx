import * as React from 'react';
import { Sello, SelloVariante } from './Sello';

export interface DiscoSelloProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** Diámetro del sello en px; el disco mide 1,25 veces más. */
  tamano?: number;
  /** Versión del sello que va encima del disco. */
  variante?: SelloVariante;
  /** Dibuja la costura fina en rojo ladrillo dentro del borde del disco (se lee como parche cosido). */
  costura?: boolean;
}

/** Sello sobre disco hueso: la forma obligatoria del logo cuando el fondo es papel de molde (#C8A97E), donde el rojo solo contrasta 2,06:1. */
export function DiscoSello({ tamano = 200, variante = 'principal', costura = true, className, style, ...rest }: DiscoSelloProps) {
  const d = Math.round(tamano * 1.25);
  const r = d / 2 - 14;
  return (
    <span
      {...rest}
      className={['atv-disco', className].filter(Boolean).join(' ')}
      style={{ width: d, height: d, borderRadius: '50%', background: 'var(--atv-hueso)', ...style }}
    >
      {costura && (
        <svg className="atv-disco-aro" viewBox={`0 0 ${d} ${d}`} aria-hidden="true" fill="none">
          <circle cx={d / 2} cy={d / 2} r={r} stroke="var(--atv-ladrillo)" strokeWidth={Math.max(2, d * 0.012)}
            strokeLinecap="round" strokeDasharray={`${d * 0.012} ${d * 0.03}`} />
        </svg>
      )}
      <Sello variante={variante} tamano={tamano} />
    </span>
  );
}
