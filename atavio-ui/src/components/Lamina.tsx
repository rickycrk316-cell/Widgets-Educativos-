import * as React from 'react';
import type { Fondo } from './tipos';

export interface LaminaProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Contenido de la pieza. La lámina es una columna con 120 px de margen; para motivos a sangre usa position:absolute. */
  children?: React.ReactNode;
  /** Color de fondo con función fija: hueso (por defecto), molde, ladrillo (portadas y cierres) o tinta (origen). Fija también el color del texto. */
  fondo?: Fondo;
  /** Formato: «feed» 1080×1350, «reel» y «historia» 1080×1920. */
  formato?: 'feed' | 'reel' | 'historia';
  /** Escala de visualización (1 = tamaño real en px; usa 0.4 para ver la pieza entera en una tarjeta). */
  escala?: number;
  /** Dibuja las zonas donde no va texto en reels (15 % superior, 35 % inferior) e historias (15 % y 25 %). */
  zonasSeguras?: boolean;
}

const ALTO = { feed: 1350, reel: 1920, historia: 1920 } as const;

/** Lienzo de una pieza de Instagram de Atavío (1080 px de ancho) con fondo de la paleta, márgenes y escala. */
export function Lamina({ children, fondo = 'hueso', formato = 'feed', escala = 1, zonasSeguras = false, className, style, ...rest }: LaminaProps) {
  const alto = ALTO[formato];
  const sup = formato === 'feed' ? 0 : Math.round(alto * 0.15);
  const inf = formato === 'reel' ? Math.round(alto * 0.35) : formato === 'historia' ? Math.round(alto * 0.25) : 0;
  return (
    <div className="atv-lamina-caja" style={{ width: 1080 * escala, height: alto * escala }}>
      <div
        {...rest}
        className={['atv-lamina', `atv-fondo-${fondo}`, className].filter(Boolean).join(' ')}
        style={{ width: 1080, height: alto, transform: `scale(${escala})`, ...style }}
      >
        {children}
        {zonasSeguras && sup > 0 && <div className="atv-guia" style={{ top: sup }}><span>sin texto arriba</span></div>}
        {zonasSeguras && inf > 0 && <div className="atv-guia" style={{ top: alto - inf }}><span>sin texto abajo</span></div>}
      </div>
    </div>
  );
}
