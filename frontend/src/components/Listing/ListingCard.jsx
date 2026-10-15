import Link from 'next/link';
import styles from './ListingCard.module.css';
import { MapPin, Maximize2, Layers } from 'lucide-react';

export default function ListingCard({ listing }) {
  return (
    <div className={styles.listingCard}>
      <div className={styles.cardHeader}>
        <h2 className={styles.listingTitle}>{listing.title}</h2>
        <span className={listing.availability_status ? styles.availableBadge : styles.unavailableBadge}>
          {listing.availability_status ? 'Available' : 'Booked'}
        </span>
      </div>
      <div className={styles.listingDetails}>
        <span><Maximize2 size={15} /> {listing.home_size} sqft</span>
        <span><Layers size={15} /> {listing.floor} floor</span>
      </div>
      <div className={styles.listingLocation}>
        <MapPin size={15} />
        <span>{listing.city}{listing.state ? `, ${listing.state}` : ''}</span>
      </div>
      <div className={styles.listingPrice}>
        <div>
          <span className={styles.priceAmount}>${Math.abs(listing.price)}</span>
          <span className={styles.pricePeriod}>/month</span>
        </div>
        <Link href={`/eazystay/protected/listings/${listing.id}`} className={styles.viewDetailsBtn}>
          View Details
        </Link>
      </div>
    </div>
  );
};
