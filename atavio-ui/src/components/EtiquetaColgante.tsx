import * as React from 'react';
import { motivos } from '../assets/motivos';
import type { Tono } from './tipos';

export interface EtiquetaColganteProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Precio ya formateado, p. ej. «$28». Va en Libre Franklin Medium, gris tinta. */
  precio?: string;
  /** Nombre corto de la prenda (una línea). */
  nombre?: string;
  /** Ancho en px; el alto es 1,53 veces el ancho. */
  ancho?: number;
  /** «claro» (cartón molde sobre hueso o molde) u «oscuro» (cartón hueso sobre tinta o ladrillo). */
  tono?: Tono;
}

/** Etiqueta colgante de cartón con ojal e hilo: el lugar fijo del precio; reemplaza al «sello de precio». */
export function EtiquetaColgante({ precio, nombre, ancho = 320, tono = 'claro', className, style, ...rest }: EtiquetaColganteProps) {
  const a = motivos[`etiqueta-${tono}`];
  return (
    <div {...rest} className={['atv-etiqueta', className].filter(Boolean).join(' ')} style={{ width: ancho, ...style }}>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox={a.viewBox} fill="none" aria-hidden="true" dangerouslySetInnerHTML={{ __html: a.inner }} />
      {nombre && (
        <div className="atv-etiqueta-zona atv-etiqueta-nombre"
          style={{ left: '20.3%', width: '59.4%', top: '33.7%', height: '11.2%', fontSize: ancho * 0.075 }}>
          {nombre}
        </div>
      )}
      {precio && (
        <div className="atv-etiqueta-zona atv-etiqueta-precio"
          style={{ left: '20.3%', width: '59.4%', top: '49%', height: '26.5%', fontSize: ancho * 0.26 }}>
          {precio}
        </div>
      )}
    </div>
  );
}
