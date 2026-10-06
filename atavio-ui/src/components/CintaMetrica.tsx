import * as React from 'react';
import { motivos } from '../assets/motivos';
import type { Tono } from './tipos';

export interface CintaMetricaProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Ancho en px (1080 en un lienzo de feed); el alto es 0,126 veces el ancho. */
  ancho?: number;
  /** «claro» (hoja molde sobre hueso) u «oscuro» (hueso sobre tinta o ladrillo). */
  tono?: Tono;
  /** Centímetro donde cae el marcador rojo (0 a 45): indica la lámina actual de un carrusel. Omítelo para una cinta sin marcador. */
  marcador?: number;
}

/** Cinta métrica de 45 cm con marcador rojo opcional: indicador de lámina en carruseles y separador; sustituye a «2 / 7». */
export function CintaMetrica({ ancho = 1080, tono = 'claro', marcador, className, style, ...rest }: CintaMetricaProps) {
  const a = motivos[`cinta-${tono}`];
  const m = motivos.marcador;
  const x = marcador === undefined ? 0 : (18 + marcador * 23.2 - 36) / 1080;
  return (
    <div {...rest} className={['atv-cinta', className].filter(Boolean).join(' ')} style={{ width: ancho, ...style }}>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox={a.viewBox} fill="none" aria-hidden="true" dangerouslySetInnerHTML={{ __html: a.inner }} />
      {marcador !== undefined && (
        <svg className="atv-marcador" xmlns="http://www.w3.org/2000/svg" viewBox={m.viewBox} fill="none" aria-hidden="true"
          style={{ left: `${x * 100}%`, width: `${(72 / 1080) * 100}%` }} dangerouslySetInnerHTML={{ __html: m.inner }} />
      )}
    </div>
  );
}
